# Open ChargePoint DataBase - OCPDB

This application aggregates chargepoint data from different sources and provices it without authentication using an
OCPI-style JSON-API and a vector tile server.

## Data sources

| name                              | uid                   | realtime | credentials | comment                                                                                                                                                                 |
|-----------------------------------|-----------------------|----------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bundesnetzagentur: API            | bnetza_api            | false    | false       | Additional config `ignore_operators:: list[str]` is supported, which will ignore given operators during import. Set to weekly download, as it does not change so often. |
| Bundesnetzagentur: Excel          | bnetza_excel          | false    | false       |                                                                                                                                                                         |
| Lichtblick                        | lichtblick            | true     | true        | Currently dysfunctional                                                                                                                                                 |
| chargecloud: Stadtwerke Pforzheim | chargecloud_pforzheim | true     | false       |                                                                                                                                                                         |
| chargecloud: Stadtwerke Stuttgart | chargecloud_stuttgart | true     | false       |                                                                                                                                                                         |
| OCHP: Albwerk                     | ochp_albwerk          | true     | true        |                                                                                                                                                                         |
| OCHP: Ladenetz                    | ochp_ladenetz         | true     | true        |                                                                                                                                                                         |
| Giro-e                            | giroe                 | true     | true        |                                                                                                                                                                         |
| OCPI: Stadtnavi                   | ocpi_stadtnavi        | true     | false       |                                                                                                                                                                         |


### Duplicate matching

There is a matching algorithm which matches live data sources with bnetza sources. You can find details at
[our matching docs](https://github.com/binary-butterfly/ocpdb/blob/main/docs/matching.md).


## API documentation

At [api.ocpdb.de](https://api.ocpdb.de/documentation/public.html) you will find an OpenAPI documentation of public endpoints you can use.


## Command line interface

The application provides a simple command line interface:

### Import all sources

```bash
flask import all
```

### Import source: static data

```bash
flask import static example_source
```

### Import source: realtime data

```bash
flask import realtime example_source
```

### Import source: images

```bash
flask import images example_source
```

### List all sources

```bash
flask source list
```

### Delete source

```bash
flask source delete example_source
```

### Matching

```bash
flask match run
```

## System requirements & installatiion

The installation process is documented at [INSTALL.md](https://github.com/binary-butterfly/ocpdb/blob/main/INSTALL.md).


## Licence

OCPDB is under AGPL. You will find details at the [LICENCE.txt](https://github.com/binary-butterfly/ocpdb/blob/main/LICENCE.txt).


## Participate

We appreciate [bug reports and feature requests](https://github.com/binary-butterfly/ocpdb/issues).
