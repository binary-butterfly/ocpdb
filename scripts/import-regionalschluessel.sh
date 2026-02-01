#!/bin/sh

if [ -f /data/.vg25-imported ]; then
    exit 0
fi

if [ ! -f /data/vg25.gpkg ]; then
    wget -q https://daten.gdz.bkg.bund.de/produkte/vg/vg25_ebenen/aktuell/vg25.utm32s.gpkg.zip -O /data/vg25.gpkg.zip
    unzip -p /data/vg25.gpkg.zip daten/DE_VG25.gpkg > /data/vg25.gpkg
    rm /data/vg25.gpkg.zip
fi

ogr2ogr -f PostgreSQL "PG:host=$POSTGRES_HOST port=5432 user='$POSTGRES_USER' password='$POSTGRES_PASSWORD' dbname='ocpdb'" -nln regionalschluessel --config OGR_TRUNCATE YES -s_srs EPSG:25832 -t_srs EPSG:4326 /data/vg25.gpkg v_vg25_gem

touch /data/.vg25-imported
