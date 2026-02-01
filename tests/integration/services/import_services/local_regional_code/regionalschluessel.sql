CREATE TABLE public.regionalschluessel (
    id integer NOT NULL,
    objektidentifikator character varying(16),
    beginnlebenszeit timestamp with time zone,
    admin_ebene_ade character varying(60),
    ade smallint,
    geofaktor_gf character varying(60),
    gf smallint,
    besondere_gebiete_bsg character varying(60),
    bsg smallint,
    "länderkürzel_lkz" character varying(2),
    "regionalschlüssel_ars" character varying(12),
    "gemeindeschlüssel_ags" character varying(8),
    verwaltungssitz_sdv_ars character varying(12),
    geografischername_gen character varying(60),
    bezeichnung character varying(60),
    identifikator_ibz smallint,
    bemerkung character varying(60),
    namensbildung_nbd character varying(60),
    nbd character varying(4),
    land character varying(2),
    regierungsbezirk character varying(1),
    kreis character varying(2),
    verwaltungsgemeinschaftteil1 character varying(2),
    verwaltungsgemeinschaftteil2 character varying(2),
    gemeinde character varying(3),
    "funk_schlüsselstelle3" character varying(60),
    fk_s3 character varying(2),
    "europ_statistikschlüssel_nuts" character varying(5),
    "regioschlüsselaufgefüllt" character varying(12),
    "gemeindeschlüsselaufgefüllt" character varying(8),
    wirksamkeit_wsk timestamp with time zone,
    geom public.geometry(MultiPolygon,4326)
);


ALTER TABLE public.regionalschluessel OWNER TO ocpdb;
COMMENT ON TABLE public.regionalschluessel IS '2024-12-31';

CREATE SEQUENCE public.regionalschluessel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.regionalschluessel_id_seq OWNER TO ocpdb;

ALTER SEQUENCE public.regionalschluessel_id_seq OWNED BY public.regionalschluessel.id;

ALTER TABLE ONLY public.regionalschluessel ALTER COLUMN id SET DEFAULT nextval('public.regionalschluessel_id_seq'::regclass);

ALTER TABLE ONLY public.regionalschluessel
    ADD CONSTRAINT regionalschluessel_pkey PRIMARY KEY (id);

CREATE INDEX regionalschluessel_geom_geom_idx ON public.regionalschluessel USING gist (geom);
