# Access Strategies

This document describes how clients should keep a local copy of OCPDB data in sync. The recommended strategy is a
combination of three access patterns:

1. **EVSE updates** at a high frequency, using the EVSE endpoints with `last_updated_since` to fetch realtime changes
   such as status updates.
2. **Location updates** at a medium frequency, using the location endpoints with `last_updated_since` to fetch changed
   static data (new locations, addresses, connectors, tariffs, ...).
3. **Full snapshots** at a low frequency, fetching the complete dataset to correct anything incremental updates
   cannot see.

None of these patterns is sufficient on its own: full snapshots are too expensive to fetch every minute, location
updates transfer a lot of unchanged static data for every single status change, and incremental updates alone will
slowly drift away from the real dataset.


## Relevant Endpoints

### Location endpoints

All list endpoints for locations support the same filter and pagination mechanism:

| Endpoint                                       | Format                    |
|------------------------------------------------|---------------------------|
| `/api/public/v1/locations`                     | OCPI 2.2 based JSON       |
| `/api/public/ocpi/2.2/locations`               | OCPI 2.2                  |
| `/api/public/ocpi/3.0/locations`               | OCPI 3.0                  |
| `/api/public/datex/v3.5/json/static`           | DATEX II 3.5 JSON         |
| `/api/public/datex/v3.7/json/static`           | DATEX II 3.7 JSON         |

The OCPI 3.0 sub-resources (`charging_stations`, `connectors`, `tariffs`, `tariff_associations`) support
`last_updated_since` as well.

### EVSE endpoints

The EVSE list endpoints return flat EVSE objects (including their connectors) without the surrounding location:

| Endpoint                                       | Format                    |
|------------------------------------------------|---------------------------|
| `/api/public/v1/evses`                         | OCPI 2.2 based JSON       |
| `/api/public/ocpi/2.2/evses`                   | OCPI 2.2                  |
| `/api/public/ocpi/3.0/evses`                   | OCPI 3.0                  |

Besides `last_updated_since`, they support `status` / `statuses`, `location_id` and the source filters.

Relevant query parameters:

| Parameter                         | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| `last_updated_since`              | ISO 8601 timestamp. Only return objects with `last_updated >=` this value.  |
| `evse_status_last_updated_since`  | Location endpoints only: locations with an EVSE status change since then.   |
| `limit`                           | Page size, default `100`, maximum `1000`.                                   |
| `offset`                          | Offset for pagination.                                                      |
| `sorted_by`                       | Sort key. Use `id` for stable pagination.                                   |
| `source_uid` / `source_uids`      | Restrict to one or more sources.                                            |

Paginated responses contain `items`, `total_count` and, if there is a next page, `next_offset` and `next_path`. Follow
`next_path` until it is missing.


## EVSE Updates (recommended for realtime data)

### Why EVSE endpoints

Realtime data in OCPDB is EVSE data: mainly `status`, but also e.g. `status_schedule`. A status change updates the
`last_updated` of the EVSE, and this timestamp is lifted to its location as well. Location updates would therefore
return the complete location object, including all charging stations, EVSEs, connectors and static attributes, for
every single status change. The EVSE endpoints only return the EVSEs which actually changed, which is orders of
magnitude less data at the same update frequency.

### How the filter works

An EVSE matches `last_updated_since` if its own `last_updated` timestamp is at or after the given value. Each EVSE is
returned completely, including its connectors, so a matching EVSE can simply replace the local copy. EVSEs are
identified by their `uid`, which is the OCPDB EVSE id and the same value used in the EVSE objects nested in locations.

### Recommended procedure

```text
evse_cursor = <start time of the last full snapshot>

every N minutes (e.g. every minute):
    request_started_at = now()
    fetch all pages of /evses?last_updated_since=<evse_cursor - overlap>&sorted_by=id&limit=1000
    for every returned EVSE:
        if an EVSE with this uid exists locally: replace it
        else: ignore it, it will arrive with the next location update
    evse_cursor = request_started_at
```

Important details:

- **EVSE updates do not create EVSEs.** EVSE objects do not contain their location, so an EVSE which is not known
  locally cannot be placed. New EVSEs always update their location as well and are therefore picked up by the next
  location update.
- **EVSE updates do not delete EVSEs.** EVSEs removed from a location are only visible via location updates or the
  full snapshot.
- If you are only interested in a subset of the data, apply the same scope filters (e.g. `source_uids`) as for
  location updates.


## Location Updates

### How the filter works

A location matches `last_updated_since` if **the location itself or at least one of its EVSEs** has a `last_updated`
timestamp greater than or equal to the given value. The response always contains the complete location object
including all charging stations, EVSEs and connectors, so a matching location can simply replace the local copy.

Because EVSE updates lift the location `last_updated`, location updates also contain every location with a status
change. That is why they should run less often than EVSE updates: their purpose is to deliver static changes, new
locations and new or removed EVSEs, not to track realtime status.

### Recommended procedure

```text
location_cursor = <start time of the last full snapshot>

every M minutes (e.g. every 15 to 60 minutes):
    request_started_at = now()
    fetch all pages of /locations?last_updated_since=<location_cursor - overlap>&sorted_by=id&limit=1000
    upsert every returned location into the local store, keyed by its id
    location_cursor = request_started_at
```

### Common rules for EVSE and location updates

- **Use the request start time as the new cursor**, not the time the last page arrived and not the highest
  `last_updated` value in the response. Everything that changes while the pages are being fetched will be picked up by
  the next run.
- **Use an overlap window** (e.g. subtract 5 to 15 minutes from the cursor). `last_updated` is taken from the source
  data whenever the source provides it, and only falls back to the OCPDB import time if it does not. A source which
  delivers its data with a delay can therefore produce `last_updated` values which already lie in the past at the
  moment they become visible in OCPDB. The overlap catches these. Since upserts are idempotent, receiving an object
  twice is harmless.
- **Keep separate cursors** for EVSE updates and location updates.
- **Sort by `id`** to get a stable order across pages.
- **Upsert, never append.** The same object will appear in multiple incremental runs.
- **Mind the order.** A location update can contain an older state of an EVSE than an EVSE update which ran shortly
  before. If this matters, only replace a local EVSE if the incoming `last_updated` is not older than the local one.

### Choosing the intervals

The intervals should match how fresh the data needs to be. EVSE status changes often, so EVSE updates should run at
the frequency at which status needs to be current, typically every minute. Static data (addresses, connectors, tariffs)
changes rarely, so location updates can run every 15 to 60 minutes. The location interval determines how long it
takes until a new location or EVSE appears in the local copy.


## Full Snapshots

### Why incremental updates are not enough

Incremental updates only ever return objects that **still exist**. They cannot tell a client about:

- **Deleted locations.** When an import no longer contains a location, OCPDB deletes it from the database. A deleted
  location will never show up in a `last_updated_since` response, so a purely incremental client keeps it forever.
- **Deleted tariffs and sub-objects.** The same applies to obsolete tariffs and to charging stations, EVSEs or
  connectors removed from a location (the latter are visible once the parent location gets updated, but only then).
- **Changes with an older `last_updated` than the cursor.** If a source delivers data with a delay larger than the
  overlap window, or corrects historic data without updating its timestamps, the change is missed.
- **Source deletions and re-imports.** When a source is deleted and re-imported, locations get new ids.
- **Client-side errors.** Failed requests, crashed sync jobs, or bugs in the local upsert logic accumulate silently.

### Recommended procedure

```text
every M hours (e.g. once per night):
    snapshot_started_at = now()
    fetch all pages of /locations?sorted_by=id&limit=10000
    replace the local dataset with the snapshot:
        upsert every returned location
        delete every local location whose id was not part of the snapshot
    evse_cursor = snapshot_started_at
    location_cursor = snapshot_started_at
```

Important details:

- **Delete what is missing.** This is the main purpose of the snapshot. Only delete after *all* pages have been fetched
  successfully. If the snapshot fails halfway, discard it and keep the current local state.
- **Reset both incremental cursors** to the start time of the snapshot, so EVSE and location updates continue
  seamlessly.
- **Scope deletions to the filter.** If the snapshot is restricted (e.g. by `source_uids` or a bounding box), only
  delete local locations that fall into the same scope.
- **Prefer a low-traffic time** for large snapshots, as they transfer the complete dataset.
- **Expect full datasets without pagination in near future**, as we are developing in the direction of full,
  cached snapshots.


### Choosing the interval

A snapshot once a day is a reasonable default. The interval determines how long a deleted location can remain in the
local copy in the worst case. Clients which need a faster reaction to deletions can shorten it, but should keep in
mind that a snapshot is orders of magnitude larger than an incremental update.


## Summary

| Aspect               | EVSE update                             | Location update                         | Full snapshot                          |
|----------------------|-----------------------------------------|-----------------------------------------|----------------------------------------|
| Purpose              | Realtime status                         | Static changes, new locations and EVSEs | Deletions, self-healing                |
| Endpoint             | `/evses`                                | `/locations`                            | `/locations`                           |
| Frequency            | About every minute                      | Every 15 to 60 minutes                  | Hours to once a day                    |
| Filter               | `last_updated_since=<cursor - overlap>` | `last_updated_since=<cursor - overlap>` | None (or same scope filter)            |
| Local operation      | Replace known EVSEs                     | Upsert locations                        | Upsert + delete missing                |
| Detects new objects  | No                                      | Yes                                     | Yes                                    |
| Detects changes      | EVSEs only                              | Yes                                     | Yes                                    |
| Detects deletions    | No                                      | Removed EVSEs only                      | Yes                                    |
| Self-healing         | No                                      | No                                      | Yes                                    |
| Cost                 | Low                                     | Medium                                  | High                                   |
| Cursor afterwards    | Start time of the request               | Start time of the request               | Start time of the snapshot (both)      |
