# Open ChargePoint DataBase - OCPDB

This application aggregates chargepoint data from different sources and provices it without authentication using an
OCPI-style JSON-API and a vector tile server.

## Data sources

| name                                | uid                     | realtime | credentials | comment                                                                                                                                                                 |
|-------------------------------------|-------------------------|----------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bundesnetzagentur: API              | bnetza_api              | false    | false       | Additional config `ignore_operators:: list[str]` is supported, which will ignore given operators during import. Set to weekly download, as it does not change so often. |
| Bundesnetzagentur: Excel            | bnetza_excel            | false    | false       |                                                                                                                                                                         |
| chargecloud: Stadtwerke Pforzheim   | chargecloud_pforzheim   | true     | false       |                                                                                                                                                                         |
| chargecloud: Stadtwerke Stuttgart   | chargecloud_stuttgart   | true     | false       |                                                                                                                                                                         |
| chargecloud: Stadtwerke Tübingen    | chargecloud_tuebingen   | true     | false       |                                                                                                                                                                         |
| chargecloud: Stadtwerke Ludwigsburg | chargecloud_ludwigsburg | true     | true        |                                                                                                                                                                         |
| PBW                                 | eaaze_pbw               | true     | true        |                                                                                                                                                                         |
| Giro-e                              | giroe                   | true     | true        |                                                                                                                                                                         |
| Heilbronn Heckarbogen               | heilbronn_neckarbogen   | true     | true        |                                                                                                                                                                         |
| Lichtblick                          | lichtblick              | true     | true        | Currently dysfunctional                                                                                                                                                 |
| OCHP: Albwerk                       | ochp_albwerk            | true     | true        |                                                                                                                                                                         |
| OCHP: Ladenetz                      | ochp_ladenetz           | true     | true        |                                                                                                                                                                         |
| OCPI: Stadtnavi                     | ocpi_stadtnavi          | true     | false       |                                                                                                                                                                         |
| OpenData Swiss                      | opendata_swiss          | true     | false       |                                                                                                                                                                         |


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


## Official Regional Code support

OCPDB extends the Location data model with a new field `official_regional_code` in non-strict mode. This field provides
the official regional code of a location, if available. Following regional codes are used:

- DEU: Regionalschlüssel


### Setup DEU: Regionalschlüssel

In Germany, we use the dataset Verwaltungsgebiete 1:25 000 by Bundesamt für Kartographie und Geodäsie (BKG) for
assigning official regional codes to locations, licenced as
[Creative Commons Namensnennung 4.0 International](https://creativecommons.org/licenses/by/4.0/). We download the data
using wget, transform the data using ogr2ogr and store it our Postgis database.

The script does not download or import the data again. If you want to update the data, you can delete
`data/regionalschluessel/vg25.gpkg` in order to trigger the download again, and `data/regionalschluessel/.vg25-imported`
to trigger the import again. You can use this mechanism for ansible automatization, too: if you drop the geopackage
at `data/regionalschluessel/vg25.gpkg` via ansible, you won't need to download the file during runtime.


## System requirements & installatiion

The installation process is documented at [INSTALL.md](https://github.com/binary-butterfly/ocpdb/blob/main/INSTALL.md).


## Logging

The application uses the logging module with some optional extensions. Logging can be configured using the `config.yml`.

The application provides some additional context and / or special output formats to log entries with custom formatters:

### Human readable formatter with injected context

Most requests or tasks have context which can be used in log entries. The simplest  is

```yaml
LOGGING:
  formatters:
    human_readable:
      (): webapp.common.logging.formatter.flask_attributes_formatter.FlaskAttributesFormatter
      format: '%(asctime)s %(levelname)s %(source)s: %(message)s'
      defaults: {'source': '-'}
  handlers:
    my_handler:
      formatter: human_readable
```

With this example, you add the `source` to every log entry (if available). Please keep in mind that you need to
add a default, because not every log entry has a source_uid context.

Following additional log context variables are available:

- `source`
- `initiator`
- `location`
- `evse`
- `image`


### OpenTelemetry formatter

You can output log entries in OpenTelemetry format, too:

```yaml
LOGGING:
  formatters:
    open_telemetry:
      (): webapp.common.logging.formatter.flask_open_telemetry_formatter.FlaskOpenTelemetryFormatter
      prefix: ocpdb
      service_name: OCPDB
  handlers:
    my_handler:
      formatter: open_telemetry
```

Context is automatically injected into log entry `Attributes`.


## Licence

OCPDB is under AGPL. You will find details at the [LICENCE.txt](https://github.com/binary-butterfly/ocpdb/blob/main/LICENCE.txt).


## Participate

We appreciate [bug reports and feature requests](https://github.com/binary-butterfly/ocpdb/issues).
