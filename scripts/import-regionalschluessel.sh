#!/bin/sh

set -eo pipefail

if [ -f /data/.vg25-imported ]; then
    exit 0
fi

if [ ! -f /data/vg25.gpkg ]; then
    wget -q "$VG25_GEOPACKAGE_URL" -O /data/vg25.gpkg -U "${VG25_GEOPACKAGE_WGET_USER_AGENT:-OCPDB}"
fi

ogr2ogr -f PostgreSQL "PG:dbname='${PGDATABASE:-ocpdb}'" -nln regionalschluessel --config OGR_TRUNCATE YES -s_srs EPSG:25832 -t_srs EPSG:4326 /data/vg25.gpkg v_vg25_gem

touch /data/.vg25-imported
