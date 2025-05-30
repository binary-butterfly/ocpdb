"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2021 binary butterfly GmbH

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from datetime import datetime, timezone

from webapp.common.config import ConfigHelper
from webapp.models.evse import EvseStatus
from webapp.models.source import SourceStatus
from webapp.prometheus_api.prometheus_models import EvseMetric, Metrics, MetricType, SourceMetric
from webapp.repositories import EvseRepository, SourceRepository


class PrometheusHandler:
    config_helper: ConfigHelper
    source_repository: SourceRepository
    evse_repository: EvseRepository

    def __init__(
        self,
        config_helper: ConfigHelper,
        source_repository: SourceRepository,
        evse_repository: EvseRepository,
    ):
        self.config_helper = config_helper
        self.source_repository = source_repository
        self.evse_repository = evse_repository

    def get_metrics(self) -> str:
        sources = self.source_repository.fetch_sources()

        last_static_update_metrics = Metrics(
            help='Last static update in seconds from now',
            type=MetricType.gauge,
            identifier='app_ocpdb_source_last_static_update',
        )
        last_realtime_update_metrics = Metrics(
            help='Last realtime update in seconds from now',
            type=MetricType.gauge,
            identifier='app_ocpdb_source_last_realtime_update',
        )
        source_static_errors = Metrics(
            help='Static errors by source',
            type=MetricType.gauge,
            identifier='app_static_ocpdb_source_errors',
        )
        source_realtime_errors = Metrics(
            help='Realtime error by source',
            type=MetricType.gauge,
            identifier='app_realtime_ocpdb_source_errors',
        )
        failed_static_sources = Metrics(
            help='Completely failed static sources',
            type=MetricType.gauge,
            identifier='app_ocpdb_static_source_failed',
        )
        failed_realtime_sources = Metrics(
            help='Completely failed realtime sources',
            type=MetricType.gauge,
            identifier='app_ocpdb_realtime_source_failed',
        )
        for source in sources:
            if source.static_status in [SourceStatus.DISABLED, SourceStatus.PROVISIONED]:
                continue

            if source.static_data_updated_at:
                last_static_update_metrics.metrics.append(
                    SourceMetric(
                        source=source.uid,
                        value=int((datetime.now(tz=timezone.utc) - source.static_data_updated_at).total_seconds()),
                    )
                )
            source_static_errors.metrics.append(
                SourceMetric(
                    source=source.uid,
                    value=source.static_error_count,
                )
            )
            failed_static_sources.metrics.append(
                SourceMetric(
                    source=source.uid,
                    value=1 if source.static_status == SourceStatus.FAILED else 0,
                )
            )

            if source.realtime_status in [SourceStatus.DISABLED, SourceStatus.PROVISIONED]:
                continue

            if source.realtime_data_updated_at:
                last_realtime_update_metrics.metrics.append(
                    SourceMetric(
                        source=source.uid,
                        value=int((datetime.now(tz=timezone.utc) - source.realtime_data_updated_at).total_seconds()),
                    )
                )
            source_realtime_errors.metrics.append(
                SourceMetric(
                    source=source.uid,
                    value=source.realtime_error_count,
                )
            )
            failed_realtime_sources.metrics.append(
                SourceMetric(
                    source=source.uid,
                    value=1 if source.realtime_status == SourceStatus.FAILED else 0,
                )
            )

        metrics = (
            failed_static_sources.to_metrics()
            + last_static_update_metrics.to_metrics()
            + source_static_errors.to_metrics()
            + failed_realtime_sources.to_metrics()
            + last_realtime_update_metrics.to_metrics()
            + source_realtime_errors.to_metrics()
        )

        if self.config_helper.get('EVSE_STATUS_METRICS', False):
            metrics += self.get_evse_status_metrics()

        return '\n'.join(metrics)

    def get_evse_status_metrics(self):
        evse_summary_list = self.evse_repository.fetch_evse_status_summary()

        available_metrics = Metrics(
            help='EVSEs with status AVAILABLE',
            type=MetricType.gauge,
            identifier='app_ocpdb_evse_status_available',
        )
        taken_metrics = Metrics(
            help='EVSEs with status CHARGING, RESERVED',
            type=MetricType.gauge,
            identifier='app_ocpdb_evse_status_taken',
        )
        error_metrics = Metrics(
            help='EVSEs with status INOPERATIVE, OUTOFORDER, REMOVED, PLANNED, BLOCKED, UNKNOWN',
            type=MetricType.gauge,
            identifier='app_ocpdb_evse_status_error',
        )
        evse_error_states = [
            EvseStatus.INOPERATIVE,
            EvseStatus.OUTOFORDER,
            EvseStatus.REMOVED,
            EvseStatus.PLANNED,
            EvseStatus.BLOCKED,
            EvseStatus.UNKNOWN,
        ]
        for evse_summary in evse_summary_list:
            available_metrics.metrics.append(
                EvseMetric(
                    evse=evse_summary.evse,
                    location=evse_summary.location,
                    source=evse_summary.source,
                    value=1 if evse_summary.status == EvseStatus.AVAILABLE else 0,
                ),
            )
            taken_metrics.metrics.append(
                EvseMetric(
                    evse=evse_summary.evse,
                    location=evse_summary.location,
                    source=evse_summary.source,
                    value=1 if evse_summary.status in [EvseStatus.CHARGING, EvseStatus.RESERVED] else 0,
                ),
            )
            error_metrics.metrics.append(
                EvseMetric(
                    evse=evse_summary.evse,
                    location=evse_summary.location,
                    source=evse_summary.source,
                    value=1 if evse_summary.status in evse_error_states else 0,
                ),
            )
        return available_metrics.to_metrics() + taken_metrics.to_metrics() + error_metrics.to_metrics()
