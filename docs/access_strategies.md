# Access Strategies

This document describes how clients should keep a local copy of OCPDB data in sync. The recommended strategy is a
combination of two access patterns:

1. **Incremental updates** at a high frequency, using the `last_updated_since` filter to fetch only what changed.
2. **Full snapshots** at a low frequency, fetching the complete dataset to correct anything incremental updates
   cannot see.

Neither pattern is sufficient on its own: full snapshots are too expensive to fetch every minute, and incremental
updates alone will slowly drift away from the real dataset.


## Relevant Endpoints

All list endpoints for locations support the same filter and pagination mechanism:

| Endpoint                                       | Format                    |
|------------------------------------------------|---------------------------|
| `/api/public/v1/locations`                     | OCPI 2.2 based JSON       |
| `/api/public/ocpi/2.2/locations`               | OCPI 2.2                  |
| `/api/public/ocpi/3.0/locations`               | OCPI 3.0                  |
| `/api/public/datex/v3.5/json/static`           | DATEX II 3.5 JSON         |
| `/api/public/datex/v3.7/json/static`           | DATEX II 3.7 JSON         |

The OCPI 3.0 sub-resources (`charging_stations`, `evses`, `connectors`, `tariffs`, `tariff_associations`) support
`last_updated_since` as well.

Relevant query parameters:

| Parameter                         | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| `last_updated_since`              | ISO 8601 timestamp. Only return objects with `last_updated >=` this value.  |
| `evse_status_last_updated_since`  | DATEX II realtime only: only EVSEs whose status changed since this value.   |
| `limit`                           | Page size, default `100`, maximum `1000`.                                   |
| `offset`                          | Offset for pagination.                                                      |
| `sorted_by`                       | Sort key. Use `id` for stable pagination.                                   |
| `source_uid` / `source_uids`      | Restrict to one or more sources.                                            |

Paginated responses contain `items`, `total_count` and, if there is a next page, `next_offset` and `next_path`. Follow
`next_path` until it is missing.


## Incremental Updates via `last_updated_since`

### How the filter works

A location matches `last_updated_since` if **the location itself or at least one of its EVSEs** has a `last_updated`
timestamp greater than or equal to the given value. The response always contains the complete location object
including all charging stations, EVSEs and connectors, so a matching location can simply replace the local copy.

### Recommended procedure

```text
cursor = <start time of the last full snapshot>

every N minutes:
    request_started_at = now()
    fetch all pages of /locations?last_updated_since=<cursor - overlap>&sorted_by=id&limit=1000
    upsert every returned location into the local store, keyed by its id
    cursor = request_started_at
```

Important details:

- **Use the request start time as the new cursor**, not the time the last page arrived and not the highest
  `last_updated` value in the response. Everything that changes while the pages are being fetched will be picked up by
  the next run.
- **Use an overlap window** (e.g. subtract 5 to 15 minutes from the cursor). `last_updated` is taken from the source
  data whenever the source provides it, and only falls back to the OCPDB import time if it does not. A source which
  delivers its data with a delay can therefore produce `last_updated` values which already lie in the past at the
  moment they become visible in OCPDB. The overlap catches these. Since upserts are idempotent, receiving a location
  twice is harmless.
- **Sort by `id`** to get a stable order across pages.
- **Upsert, never append.** The same location will appear in multiple incremental runs.

### Choosing the interval

The interval should match how fresh the data needs to be. Static data (addresses, connectors, tariffs) changes rarely,
EVSE status changes often. For realtime status, DATEX II realtime endpoints with `evse_status_last_updated_since`
provide a lighter-weight delta than full location objects.


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
    fetch all pages of /locations?sorted_by=id&limit=1000
    replace the local dataset with the snapshot:
        upsert every returned location
        delete every local location whose id was not part of the snapshot
    cursor = snapshot_started_at
```

Important details:

- **Delete what is missing.** This is the main purpose of the snapshot. Only delete after *all* pages have been fetched
  successfully. If the snapshot fails halfway, discard it and keep the current local state.
- **Reset the incremental cursor** to the start time of the snapshot, so incremental updates continue seamlessly.
- **Scope deletions to the filter.** If the snapshot is restricted (e.g. by `source_uids` or a bounding box), only
  delete local locations that fall into the same scope.
- **Prefer a low-traffic time** for large snapshots, as they transfer the complete dataset.

### Choosing the interval

A snapshot once a day is a reasonable default. The interval determines how long a deleted location can remain in the
local copy in the worst case. Clients which need a faster reaction to deletions can shorten it, but should keep in
mind that a snapshot is orders of magnitude larger than an incremental update.


## Summary

| Aspect               | Incremental update                          | Full snapshot                               |
|----------------------|---------------------------------------------|---------------------------------------------|
| Frequency            | Minutes                                     | Hours to once a day                         |
| Filter               | `last_updated_since=<cursor - overlap>`     | None (or same scope filter as incremental)  |
| Local operation      | Upsert                                      | Upsert + delete missing                     |
| Detects new/changed  | Yes                                         | Yes                                         |
| Detects deletions    | No                                          | Yes                                         |
| Self-healing         | No                                          | Yes                                         |
| Cost                 | Low                                         | High                                        |
| Cursor afterwards    | Start time of the request                   | Start time of the snapshot                  |
