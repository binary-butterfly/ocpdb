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

from flask import make_response

from webapp.common.base_blueprint import BaseBlueprint
from webapp.common.rest import BaseMethodView
from webapp.dependencies import dependencies
from webapp.prometheus_api.prometheus_handler import PrometheusHandler


class PrometheusRestApi(BaseBlueprint):
    documentation_base = True

    def __init__(self):
        super().__init__('prometheus', __name__, url_prefix='/metrics')

        prometheus_handler = PrometheusHandler(
            **self.get_base_handler_dependencies(),
            evse_repository=dependencies.get_evse_repository(),
            source_repository=dependencies.get_source_repository(),
        )

        self.add_url_rule(
            '',
            view_func=MetricsMethodView.as_view(
                'metrics',
                **self.get_base_method_view_dependencies(),
                prometheus_handler=prometheus_handler,
            ),
        )


class MetricsMethodView(BaseMethodView):
    prometheus_handler: PrometheusHandler

    def __init__(self, *, prometheus_handler: PrometheusHandler, **kwargs):
        super().__init__(**kwargs)
        self.prometheus_handler = prometheus_handler

    def get(self):
        response_string = self.prometheus_handler.get_metrics()
        response = make_response(response_string)
        response.mimetype = 'text/plain; version=0.0.4'
        return response
