# DATEX II 3.5 Import

OCPDB ingests charging-infrastructure data in the
[DATEX II German Energy Infrastructure Profile](https://github.com/MobilithekDE/AFIR-DATEX-II-Recharging-Profil/)
(JSON, version 3.5). This document describes **how** data reaches OCPDB (access mechanisms, transport, data flow and
source-status bookkeeping). The field-level translation between the DATEX II payload and the OCPDB / OCPI data model
is documented separately in [`docs/input_mapping/datex2_3.5.md`](input_mapping/datex2_3.5.md).

The import logic lives in
[`webapp/services/import_services/datex2/base_datex2_v3_5_import_service.py`](../webapp/services/import_services/datex2/base_datex2_v3_5_import_service.py).
The push endpoint lives in
[`webapp/server_rest_api/datex2/`](../webapp/server_rest_api/datex2/).

## Data model overview

| Dataset  | Publication type                              | Wrapper                                     |
|----------|-----------------------------------------------|---------------------------------------------|
| Static   | `aegiEnergyInfrastructureTablePublication`    | `DATEXII3D2PayloadInput`                    |
| Realtime | `aegiEnergyInfrastructureStatusPublication`   | `MessageContainerWrapperOutput` (payload[]) |

Static data defines the location/station/EVSE/connector tree. Realtime data carries per-refill-point statuses that
reference the static tree via IDs.

## Transport: Mobilithek subscriptions (pull)

Both static and realtime data are offered as per-source *subscriptions* on the federal Mobilithek broker:

```
https://mobilithek.info:8443/mobilithek/api/v1.0/subscription?subscriptionID=<id>
```

Access is authenticated via **mutual TLS**. The service reads the client certificate and private key paths from the
source configuration and passes them to `requests` as `cert=(cert_path, key_path)`. Each source declares its own
subscription IDs so one OCPDB instance can pull from multiple DATEX II providers in parallel.

### Source configuration

```yaml
SOURCES:
  datex2_enbw:
    static_subscription_id: 12345
    realtime_subscription_id: 67890
    mobilithek_cert_path: /path/to/client.crt
    mobilithek_key_path:  /path/to/client.key
    # Optional: disables the realtime pull loop if the upstream only pushes.
    use_realtime_push: false
    # Required only for the push endpoint (see below).
    api_key: <shared-secret>
```

Missing `static_subscription_id` or `realtime_subscription_id` raises `IncompleteConfigException` when the
corresponding fetch runs.

## Static data flow — `fetch_static_data()`

1. Read `static_subscription_id`; abort with `IncompleteConfigException` if absent.
2. `request_data(subscription_id)` issues a single GET against the subscription URL (mTLS).
3. Validate the body against `DATEXII3D2PayloadInput`. On `ValidationError` or a missing / multiple
   `energyInfrastructureTable` entries the source is marked `FAILED` for both static and realtime.
4. Iterate `energyInfrastructureSite` entries, map each one to a `LocationUpdate` via
   `Datex2V35JSONStaticMapper` (see mapping doc) and collect successful mappings.
5. Persist via `save_location_updates(...)`.
6. Update the source: `static_status = ACTIVE`, `static_data_updated_at =` server's `Last-Modified` (or `None`).

There is no loop — a static pull is one request per run.

## Realtime data flow — `fetch_realtime_data()`

Realtime is the more intricate flow because a single subscription response can be smaller than the full delta and
Mobilithek pages via the standard HTTP `If-Modified-Since` / `Last-Modified` mechanism. The import therefore runs
a **multi-dataset catch-up loop**.

Preconditions:

- Source's `static_status` must be `ACTIVE`, otherwise the fetch returns without touching anything.
- If `use_realtime_push: true` is set, the pull is skipped entirely (the server expects REST pushes instead).
- `realtime_subscription_id` must be configured.

Loop body (up to 25 000 iterations as a safety cap):

1. Determine `if_modified_since`:
   - first ever run → `now - 1h`
   - subsequent runs → `source.realtime_data_updated_at`
   - within the loop → the previous response's `Last-Modified`
2. GET the realtime subscription URL with `If-Modified-Since: <RFC 5322>` and mTLS.
3. A missing `Last-Modified` response header is treated as a protocol error: the source is marked `FAILED` and the
   loop aborts. (HTTP-level failures / `RemoteException` do the same.)
4. Parse the body as `MessageContainerWrapperOutput` and feed it to `add_realtime_data(data, result)`:
   - validates the wrapper + first payload,
   - walks `energyInfrastructureSiteStatus → energyInfrastructureStationStatus → refillPointStatus`,
   - maps each refill-point status to an `EvseRealtimeUpdate`,
   - accumulates updates in `result.evse_updates_by_evse` keyed by `evse_id` (later wins), and counts
     success / error outcomes.
5. **Exit condition:** when the server's `Last-Modified` equals the `If-Modified-Since` we sent, we've caught up
   and the loop breaks. Otherwise `if_modified_since` advances to the new `Last-Modified` and we request again.
6. After the loop: `save_evse_updates(list(result.evse_updates_by_evse.values()))`, then update the source with
   `realtime_status = ACTIVE`, the error count, and `realtime_data_updated_at =` the final `Last-Modified`.

Because updates are deduplicated by EVSE ID inside the loop, the database sees one write per EVSE per run even if
the same EVSE's status is reported across several pages.

## Push endpoint: `webapp/server_rest_api/datex2`

For operators that *push* realtime data (including Mobilithek itself, when acting as a relay), OCPDB exposes a
realtime-only REST endpoint.

```
POST /api/server/v1/datex/v3.5/<source_uid>/realtime?key=<api_key>
Content-Type: application/json
```

- **Authentication.** The handler in
  [`datex2_handler.py`](../webapp/server_rest_api/datex2/datex2_handler.py) compares the `key` query parameter
  against the source's configured `api_key`, because Mobilithek does not support BasicAuth or Token auth. Missing or
- mismatched → `401 Unauthorized`. Basic-auth is deliberately skipped on this view (`skip_basic_auth`).
- **Payload.** Same `MessageContainerWrapperOutput` shape as the pull path. Validation errors produce
  `ImportException` and mark the source as `FAILED`.
- **Processing.** Calls `service.add_realtime_data(data, result)` exactly once (the server API handles a single
  dataset per request — the multi-dataset loop stays inside the pull service), then `save_evse_updates` and
  `update_source`. `realtime_data_updated_at` is taken from the payload's `publicationTime` when present, otherwise
  from the wall clock.
- **Response.** `HTTP 200` with an empty JSON body (`{}`). Note this is intentionally **not** `204`: Mobilithek's
  push client treats anything other than `200` as an error.

When `use_realtime_push: true` is set on a source, the pull loop is disabled and only this endpoint updates
realtime data.

### Gzip-encoded request bodies

Mobilithek pushes large realtime payloads with `Content-Encoding: gzip`. The request body is decompressed
transparently by a `before_request` hook registered on the `/api/server/v1` blueprint in
[`webapp/server_rest_api/server_rest_api.py`](../webapp/server_rest_api/server_rest_api.py):

```python
@self.before_request
def decode_gzip() -> None:
    if not request.path.startswith('/api/server/v1'):
        return
    if getattr(request, 'content_encoding', None) != 'gzip':
        return
    request.stream = GzipFile(fileobj=request.stream)
```

Because this is wired up at the server-api blueprint level, the DATEX II realtime endpoint **must be reached via
`/api/server/v1/datex/...`** for gzip handling to kick in. Clients should set:

```
Content-Encoding: gzip
Content-Type: application/json
```

and submit the gzip-compressed JSON body. The handler itself sees a normal decoded JSON document.

## Source-status bookkeeping

| Condition                                                      | `static_status` | `realtime_status` |
|----------------------------------------------------------------|-----------------|-------------------|
| Static fetch fails (transport, validation, shape)              | `FAILED`        | `FAILED`          |
| Static fetch succeeds                                          | `ACTIVE`        | unchanged         |
| Realtime fetch runs while `static_status != ACTIVE`            | unchanged       | unchanged (skip)  |
| Realtime transport error / missing `Last-Modified` / bad body  | unchanged       | `FAILED`          |
| Realtime fetch or push succeeds                                | unchanged       | `ACTIVE`          |

`realtime_data_updated_at` always stores the upstream `Last-Modified` (pull) or `publicationTime` (push), never the
local wall-clock time, so the next pull can resume correctly via `If-Modified-Since`.

## Extending for a new DATEX II source

Subclass `BaseDatex2V35ImportService`, set a distinct `source_info.uid`, register the class in the importer
registry, and add a block under `SOURCES:` in `config.yaml` with the subscription IDs and mTLS cert paths (and
optionally `api_key` / `use_realtime_push`). All transport, validation, loop control, gzip decoding and status
bookkeeping are inherited — only source-specific mapping quirks (if any) need overriding.
