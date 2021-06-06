-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: mysql
-- Erstellungszeit: 06. Jun 2021 um 15:19
-- Server-Version: 10.3.11-MariaDB-1:10.3.11+maria~bionic
-- PHP-Version: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Datenbank: `ocpdb`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Daten für Tabelle `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('6fcdaafd45ac');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `business`
--

CREATE TABLE `business` (
  `id` bigint(20) NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  `logo_id` bigint(20) DEFAULT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `website` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `chargepoint`
--

CREATE TABLE `chargepoint` (
  `id` bigint(20) NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  `location_id` bigint(20) DEFAULT NULL,
  `external_id` bigint(20) DEFAULT NULL,
  `uid` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `giroe_id` bigint(20) DEFAULT NULL,
  `evse_id` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `status` enum('AVAILABLE','BLOCKED','CHARGING','INOPERATIVE','OUTOFORDER','PLANNED','REMOVED','RESERVED','UNKNOWN') COLLATE utf8_unicode_ci DEFAULT NULL,
  `lat` decimal(9,7) DEFAULT NULL,
  `lon` decimal(10,7) DEFAULT NULL,
  `floor_level` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
  `physical_reference` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `directions` text COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `parking_uid` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `parking_floor_level` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `parking_spot_number` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `max_reservation` float DEFAULT NULL,
  `capabilities` int(11) DEFAULT NULL,
  `parking_restrictions` int(11) DEFAULT NULL,
  `terms_and_conditions` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `chargepoint_image`
--

CREATE TABLE `chargepoint_image` (
  `chargepoint_id` bigint(20) DEFAULT NULL,
  `image_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `connector`
--

CREATE TABLE `connector` (
  `id` bigint(20) NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  `chargepoint_id` bigint(20) DEFAULT NULL,
  `uid` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `giroe_id` bigint(20) DEFAULT NULL,
  `standard` enum('CHADEMO','DOMESTIC_A','DOMESTIC_B','DOMESTIC_C','DOMESTIC_D','DOMESTIC_E','DOMESTIC_F','DOMESTIC_G','DOMESTIC_H','DOMESTIC_I','DOMESTIC_J','DOMESTIC_K','DOMESTIC_L','IEC_60309_2_single_16','IEC_60309_2_three_16','IEC_60309_2_three_32','IEC_60309_2_three_64','IEC_62196_T1','IEC_62196_T1_COMBO','IEC_62196_T2','IEC_62196_T2_COMBO','IEC_62196_T3A','IEC_62196_T3C','PANTOGRAPH_BOTTOM_UP','PANTOGRAPH_TOP_DOWN','TESLA_R','TESLA_S') COLLATE utf8_unicode_ci DEFAULT NULL,
  `format` enum('SOCKET','CABLE') COLLATE utf8_unicode_ci DEFAULT NULL,
  `power_type` enum('AC_1_PHASE','AC_3_PHASE','DC') COLLATE utf8_unicode_ci DEFAULT NULL,
  `max_voltage` int(11) DEFAULT NULL,
  `max_amperage` int(11) DEFAULT NULL,
  `max_electric_power` int(11) DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `terms_and_conditions` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `exceptional_period`
--

CREATE TABLE `exceptional_period` (
  `id` bigint(20) NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  `location_id` bigint(20) DEFAULT NULL,
  `type` enum('opening','closing') COLLATE utf8_unicode_ci DEFAULT NULL,
  `period_begin` datetime DEFAULT NULL,
  `period_end` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `image`
--

CREATE TABLE `image` (
  `id` bigint(20) NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  `external_url` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `type` varchar(4) COLLATE utf8_unicode_ci DEFAULT NULL,
  `category` enum('CHARGER','ENTRANCE','LOCATION','NETWORK','OPERATOR','OTHER','OWNER') COLLATE utf8_unicode_ci DEFAULT NULL,
  `width` int(11) DEFAULT NULL,
  `height` int(11) DEFAULT NULL,
  `last_download` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `location`
--

CREATE TABLE `location` (
  `id` bigint(20) NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  `uid` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `giroe_id` bigint(20) DEFAULT NULL,
  `operator_id` bigint(20) DEFAULT NULL,
  `suboperator_id` bigint(20) DEFAULT NULL,
  `owner_id` bigint(20) DEFAULT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `address` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `postal_code` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `city` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `state` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `country` varchar(2) COLLATE utf8_unicode_ci DEFAULT NULL,
  `lat` decimal(9,7) DEFAULT NULL,
  `lon` decimal(10,7) DEFAULT NULL,
  `directions` text COLLATE utf8_unicode_ci DEFAULT NULL,
  `parking_type` enum('ALONG_MOTORWAY','PARKING_GARAGE','PARKING_LOT','ON_DRIVEWAY','ON_STREET','UNDERGROUND_GARAGE') COLLATE utf8_unicode_ci DEFAULT NULL,
  `time_zone` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `terms_and_conditions` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `twentyfourseven` tinyint(1) DEFAULT NULL,
  `geometry` point NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `location_image`
--

CREATE TABLE `location_image` (
  `location_id` bigint(20) DEFAULT NULL,
  `image_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `option`
--

CREATE TABLE `option` (
  `id` bigint(20) NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  `key` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `type` enum('string','date','datetime','integer','decimal','dict','list') COLLATE utf8_unicode_ci DEFAULT NULL,
  `value` text COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `regular_hours`
--

CREATE TABLE `regular_hours` (
  `id` bigint(20) NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  `location_id` bigint(20) DEFAULT NULL,
  `weekday` smallint(6) DEFAULT NULL,
  `period_begin` int(11) DEFAULT NULL,
  `period_end` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `related_resource`
--

CREATE TABLE `related_resource` (
  `id` bigint(20) NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  `chargepoint_id` bigint(20) DEFAULT NULL,
  `url` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `types` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indizes für die Tabelle `business`
--
ALTER TABLE `business`
  ADD PRIMARY KEY (`id`),
  ADD KEY `logo_id` (`logo_id`);

--
-- Indizes für die Tabelle `chargepoint`
--
ALTER TABLE `chargepoint`
  ADD PRIMARY KEY (`id`),
  ADD KEY `location_id` (`location_id`);

--
-- Indizes für die Tabelle `chargepoint_image`
--
ALTER TABLE `chargepoint_image`
  ADD KEY `chargepoint_id` (`chargepoint_id`),
  ADD KEY `image_id` (`image_id`);

--
-- Indizes für die Tabelle `connector`
--
ALTER TABLE `connector`
  ADD PRIMARY KEY (`id`),
  ADD KEY `chargepoint_id` (`chargepoint_id`);

--
-- Indizes für die Tabelle `exceptional_period`
--
ALTER TABLE `exceptional_period`
  ADD PRIMARY KEY (`id`),
  ADD KEY `location_id` (`location_id`);

--
-- Indizes für die Tabelle `image`
--
ALTER TABLE `image`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`id`),
  ADD KEY `operator_id` (`operator_id`),
  ADD KEY `owner_id` (`owner_id`),
  ADD KEY `suboperator_id` (`suboperator_id`),
  ADD SPATIAL KEY `geometry_index` (`geometry`);

--
-- Indizes für die Tabelle `location_image`
--
ALTER TABLE `location_image`
  ADD KEY `image_id` (`image_id`),
  ADD KEY `location_id` (`location_id`);

--
-- Indizes für die Tabelle `option`
--
ALTER TABLE `option`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_option_key` (`key`);

--
-- Indizes für die Tabelle `regular_hours`
--
ALTER TABLE `regular_hours`
  ADD PRIMARY KEY (`id`),
  ADD KEY `location_id` (`location_id`);

--
-- Indizes für die Tabelle `related_resource`
--
ALTER TABLE `related_resource`
  ADD PRIMARY KEY (`id`),
  ADD KEY `chargepoint_id` (`chargepoint_id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `business`
--
ALTER TABLE `business`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `chargepoint`
--
ALTER TABLE `chargepoint`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `connector`
--
ALTER TABLE `connector`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `exceptional_period`
--
ALTER TABLE `exceptional_period`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `image`
--
ALTER TABLE `image`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `location`
--
ALTER TABLE `location`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `option`
--
ALTER TABLE `option`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `regular_hours`
--
ALTER TABLE `regular_hours`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `related_resource`
--
ALTER TABLE `related_resource`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `business`
--
ALTER TABLE `business`
  ADD CONSTRAINT `business_ibfk_1` FOREIGN KEY (`logo_id`) REFERENCES `image` (`id`);

--
-- Constraints der Tabelle `chargepoint`
--
ALTER TABLE `chargepoint`
  ADD CONSTRAINT `chargepoint_ibfk_1` FOREIGN KEY (`location_id`) REFERENCES `location` (`id`);

--
-- Constraints der Tabelle `chargepoint_image`
--
ALTER TABLE `chargepoint_image`
  ADD CONSTRAINT `chargepoint_image_ibfk_1` FOREIGN KEY (`chargepoint_id`) REFERENCES `chargepoint` (`id`),
  ADD CONSTRAINT `chargepoint_image_ibfk_2` FOREIGN KEY (`image_id`) REFERENCES `image` (`id`);

--
-- Constraints der Tabelle `connector`
--
ALTER TABLE `connector`
  ADD CONSTRAINT `connector_ibfk_1` FOREIGN KEY (`chargepoint_id`) REFERENCES `chargepoint` (`id`);

--
-- Constraints der Tabelle `exceptional_period`
--
ALTER TABLE `exceptional_period`
  ADD CONSTRAINT `exceptional_period_ibfk_1` FOREIGN KEY (`location_id`) REFERENCES `location` (`id`);

--
-- Constraints der Tabelle `location`
--
ALTER TABLE `location`
  ADD CONSTRAINT `location_ibfk_1` FOREIGN KEY (`operator_id`) REFERENCES `business` (`id`),
  ADD CONSTRAINT `location_ibfk_2` FOREIGN KEY (`owner_id`) REFERENCES `business` (`id`),
  ADD CONSTRAINT `location_ibfk_3` FOREIGN KEY (`suboperator_id`) REFERENCES `business` (`id`);

--
-- Constraints der Tabelle `location_image`
--
ALTER TABLE `location_image`
  ADD CONSTRAINT `location_image_ibfk_1` FOREIGN KEY (`image_id`) REFERENCES `image` (`id`),
  ADD CONSTRAINT `location_image_ibfk_2` FOREIGN KEY (`location_id`) REFERENCES `location` (`id`);

--
-- Constraints der Tabelle `regular_hours`
--
ALTER TABLE `regular_hours`
  ADD CONSTRAINT `regular_hours_ibfk_1` FOREIGN KEY (`location_id`) REFERENCES `location` (`id`);

--
-- Constraints der Tabelle `related_resource`
--
ALTER TABLE `related_resource`
  ADD CONSTRAINT `related_resource_ibfk_1` FOREIGN KEY (`chargepoint_id`) REFERENCES `chargepoint` (`id`);
COMMIT;
