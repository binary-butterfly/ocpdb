# Changelog

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
