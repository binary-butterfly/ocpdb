# Changelog

## 2.11.0

Released 2026-04-27

### Features

* Several new Datex2 data sources (see README.md for details)


### Fixes

* Location API SQL Query optimization
* Optimizations and fixes for Datex2 validation system


## 2.10.2

Released 2026-04-20

### Fixes

* Fix endpoint for Mobilithek by adding gzip support
* Fix access management by adding key support
* Fix Datex2 client by adding iteration mechanism for delta push updates
* Fix MessageContainer output


## 2.10.1

Released 2026-04-14

### Fixes

* [Fix multiple issues with datex2 outputs, with new mobilithek-optimized realtime endpoint](https://github.com/binary-butterfly/ocpdb/pull/191)


## 2.10.0

Released 2026-04-13

### Features

* [Datex2 Tariff](https://github.com/binary-butterfly/ocpdb/pull/190)


## Version 2.9.0

Released 2026-03-23

This release adds DATEX2 support:

* EnBW DATEX2 import
* DATEX2 3.5 static and realtime APIs
* DATEX2 3.7 static API


### Features

* [first generic datex steps](https://github.com/binary-butterfly/ocpdb/pull/170)


## Version 2.8.0

Released 2026-03-16

### Features

* [Official region code Support for Germany (Regionalschlüssel)](https://github.com/binary-butterfly/ocpdb/pull/183)


### Maintenance

* [Update dependencies](https://github.com/binary-butterfly/ocpdb/pull/189)


## Version 2.7.2

Released 2026-03-12

### Fixes

* [Further ocpi 3 0 improvements](https://github.com/binary-butterfly/ocpdb/pull/188)


## Version 2.7.1

Released 2026-03-12

### Fixes

* [OCPI 3.0 improvements](https://github.com/binary-butterfly/ocpdb/pull/185)
* [More compliant OCPI periods, fix bnetza time](https://github.com/binary-butterfly/ocpdb/pull/186)
* [group bnetza locations](https://github.com/binary-butterfly/ocpdb/pull/187)


## Version 2.7.0

Released 2026-03-08

Internal data model changes from OCPI 2.2 to OCPI 3.0. The API is not affected.

### Features

* [OCPI 3.0 Support](https://github.com/binary-butterfly/ocpdb/pull/184)


## Version 2.6.0

Released 2026-02-02

### Features

* [Sources API](https://github.com/binary-butterfly/ocpdb/pull/168)
* [Better logging, including more context and docs](https://github.com/binary-butterfly/ocpdb/pull/169)
* [bounding box search](https://github.com/binary-butterfly/ocpdb/pull/177)
* [Last modified search](https://github.com/binary-butterfly/ocpdb/pull/178)
* [Evse endpoint ](https://github.com/binary-butterfly/ocpdb/pull/179)
* [optimize related resource](https://github.com/binary-butterfly/ocpdb/pull/180)
* [optimize opening hours](https://github.com/binary-butterfly/ocpdb/pull/181)


### Fixes

* [fix performance issue with char filter](https://github.com/binary-butterfly/ocpdb/pull/171)
* [re-add index](https://github.com/binary-butterfly/ocpdb/pull/172)
* [BNetzA: filter more characters](https://github.com/binary-butterfly/ocpdb/pull/173)
* [Optimize last updated](https://github.com/binary-butterfly/ocpdb/pull/182)


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
