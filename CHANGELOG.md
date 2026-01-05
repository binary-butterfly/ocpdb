# Changelog

## Version 2.5.1

Released 2026-01-05

### Fixes

* [Fix Ladenetz Charset](https://github.com/binary-butterfly/ocpdb/pull/167


## Version 2.5.0

Released 2025-11-22

### Features

* [eaaze pbw](https://github.com/binary-butterfly/ocpdb/pull/160))


### Fixes

* [location test, test and fix OpenAPI](https://github.com/binary-butterfly/ocpdb/pull/162)
* [Fix search filter](https://github.com/binary-butterfly/ocpdb/pull/161)
* [Foreign key indices](https://github.com/binary-butterfly/ocpdb/pull/159)
* [Optimize Location Query](https://github.com/binary-butterfly/ocpdb/pull/158)


## Version 2.4.0

Released 2025-11-17

### Features

* [Filter by operator name](https://github.com/binary-butterfly/ocpdb/pull/156)


### Fixes

* [Improve PrintableStringValidator](https://github.com/binary-butterfly/ocpdb/pull/154)
* [Use PrintableStringValidator at more places at XLSX import](https://github.com/binary-butterfly/ocpdb/pull/155)


### Maintenance

* [Updates and maintenance](https://github.com/binary-butterfly/ocpdb/pull/157)


## Version 2.3.1

Released 2025-10-27

### Fixes

* [better geo-validation](https://github.com/binary-butterfly/ocpdb/pull/151)


## Version 2.3.0

### Features

* [more search params](https://github.com/binary-butterfly/ocpdb/pull/133)
* [chargecloud tuebingen importer](https://github.com/binary-butterfly/ocpdb/pull/134)


## Version 2.2.2

### Fixes

* [fix bnetza after api change](https://github.com/binary-butterfly/ocpdb/pull/132)


## Version 2.2.1

### Fixes

* [Fix OpenData Swiss Overwriting](https://github.com/binary-butterfly/ocpdb/pull/127)


## Version 2.2.0

### Features

* [Additional source filter](https://github.com/binary-butterfly/ocpdb/pull/124)


### Fixes

* [OpenData Swiss static status](https://github.com/binary-butterfly/ocpdb/pull/125)


### Maintenance

* [Dependency updates](https://github.com/binary-butterfly/ocpdb/pull/125)


## Version 2.1.2

### Fixes

* [Several smaller fixes](https://github.com/binary-butterfly/ocpdb/pull/116)
  * fetch_at_init support
  * OpenData Swiss Reserved Enum
  * prevent duplicate logging at celery dev server
  * more fitting log levels


## Version 2.1.1

### Fixes

* [more efficient evse status updates, fixing BNetzA Cron, other small fixes](https://github.com/binary-butterfly/ocpdb/pull/113)


## Version 2.1.0

### Features

* [Simple ignore mechanism for BNetzA operators](https://github.com/binary-butterfly/ocpdb/pull/112)


## Version 2.0.0

Released 2025-05-18

### Features

* [New Logging system with OpenTelemetry Support](https://github.com/binary-butterfly/ocpdb/pull/102), see
* [New config file layout](https://github.com/binary-butterfly/ocpdb/blob/main/INSTALL.md#configuration)
* [New debug system for dumping full communication per source](https://github.com/binary-butterfly/ocpdb/blob/main/INSTALL.md#configuration)
* [OpenData Swiss](https://github.com/binary-butterfly/ocpdb/pull/106)
* [Heilbronn Neckarbogen](https://github.com/binary-butterfly/ocpdb/pull/105)

The old sources definition is still supported but will throw deprecation warnings. Please have a close look, as
some mechanisms like the url work differently now (which makes this release breaking)

Several converters were renamed, which makes this release breaking, too.
[See README for details](https://github.com/binary-butterfly/ocpdb/blob/main/README.md#data-sources).


## Version 1.5.1

Released 2025-04-29

### Fixes

* [prevent ochp import error at empty data source](https://github.com/binary-butterfly/ocpdb/pull/103)


## Version 1.5.0

Released 2025-04-28

### Features

* [BNetzA import via API](https://github.com/binary-butterfly/ocpdb/pull/101)
* Loads config.secrets.yaml as an additional file for secrets

### Fixes

* Fixes the `flask source fetch-all` endpoint


### Maintenance

* Integration tests now run via CI


## Version 1.4.1

Released 2025-04-14

### Fixes

* [Fix Giro-e import / make it work with new hearbeat system](https://github.com/binary-butterfly/ocpdb/pull/98)


## Version 1.4.0

Released 2025-04-12

In this release, we migrated to SQLAlchemy2 and add two new data sources.

### Features

* [SQLAlchemy2 migration](https://github.com/binary-butterfly/ocpdb/pull/95)
* [Support Albwerk](https://github.com/binary-butterfly/ocpdb/pull/94)
* [Support Pforzheim](https://github.com/binary-butterfly/ocpdb/pull/96)


## Version 1.3.0

Released 2025-01-25

In this release, the OCPDB gets closer to the OCPI data model, which includes typing fixes as well as
the intruction of a strict mode, which filters all non-OCPI-compliant fields.

### Features

* [Mitigate OCPI compatibility issues](https://github.com/binary-butterfly/ocpdb/pull/82)


## Version 1.2.3

Released 2025-01-21

### Features

* [sw_stuttgart: add max_electric_power and mapping docs](https://github.com/binary-butterfly/ocpdb/pull/80)


## Version 1.2.2

Released 2024-12-31

### Features

* [Fixes an issue with default minute value at crontab](https://github.com/binary-butterfly/ocpdb/pull/76)


## Version 1.2.1

Released 2024-12-26

### Features

* [Provides an abstract command line interface for data sources](https://github.com/binary-butterfly/ocpdb/pull/75)


## Version 1.2.0

Released 2024-12-19

### Features

* [Stadtwerke Stuttgart Source](https://github.com/binary-butterfly/ocpdb/pull/69)
* [Cron Mechanism](https://github.com/binary-butterfly/ocpdb/pull/73)

### Fixes

* [BNetzA Import Fix](https://github.com/binary-butterfly/ocpdb/pull/71)


### Maintenance

* Several dependency updates
* [Replacement of vector tile library](https://github.com/binary-butterfly/ocpdb/pull/67)
* [Ruff linting and formatting](https://github.com/binary-butterfly/ocpdb/pull/72)


## Version 1.1.0

Released 2024-07-21

### Features

* Introduce sources in database to get statistics per source
* Metrics endpoint for sources and EVSEs
* Giro-e PubSub connection for realtime status updates

### Maintenance

* Several dependency updates
* Old code cleanup
* Introduce ruff in CI
* Finalized moving OCPDB to Github


## Version 1.0.0

Released 2024-05-01

First release with SemVer versioning.
