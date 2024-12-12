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

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import List


class MetricType(Enum):
    gauge = 'gauge'


@dataclass
class BaseMetric:
    value: int

    def to_metric(self, identifier: str) -> str:
        data = asdict(self)
        label_list: List[str] = []
        for key, value in data.items():
            if key == 'value':
                continue
            value = value.replace('"', '')
            label_list.append(f'{key}="{value}"')
        return f'{identifier}{{{",".join(label_list)}}} {self.value}'


@dataclass
class SourceMetric(BaseMetric):
    source: str


@dataclass
class EvseMetric(SourceMetric):
    evse: str
    location: str


@dataclass
class Metrics:
    help: str
    type: MetricType
    identifier: str
    metrics: List[BaseMetric] = field(default_factory=list)

    def to_metrics(self) -> List[str]:
        return [f'# HELP {self.identifier} {self.help}', f'# TYPE {self.identifier} {self.type.name}'] + [
            metric.to_metric(self.identifier) for metric in self.metrics
        ]
