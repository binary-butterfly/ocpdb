"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.dynamic_activation_status_publication_input import (
    DynamicActivationStatusPublicationInput,
)
from webapp.shared.datex2.v3_7.shared.fault_publication_input import FaultPublicationInput
from webapp.shared.datex2.v3_7.shared.generic_publication_input import GenericPublicationInput
from webapp.shared.datex2.v3_7.shared.predefined_condition_publication_input import PredefinedConditionPublicationInput
from webapp.shared.datex2.v3_7.shared.status_publication_input import StatusPublicationInput

from .controlled_zone_table_publication_input import ControlledZoneTablePublicationInput
from .device_publication_input import DevicePublicationInput
from .elaborated_data_publication_input import ElaboratedDataPublicationInput
from .energy_infrastructure_status_publication_input import EnergyInfrastructureStatusPublicationInput
from .energy_infrastructure_table_publication_input import EnergyInfrastructureTablePublicationInput
from .measured_data_publication_input import MeasuredDataPublicationInput
from .measurement_site_table_publication_input import MeasurementSiteTablePublicationInput
from .operating_hours_publication_input import OperatingHoursPublicationInput
from .organisation_publication_input import OrganisationPublicationInput
from .parking_status_publication_input import ParkingStatusPublicationInput
from .parking_table_publication_input import ParkingTablePublicationInput
from .predefined_locations_publication_input import PredefinedLocationsPublicationInput
from .rates_publication_input import RatesPublicationInput
from .situation_publication_input import SituationPublicationInput
from .tmplan_operation_publication_input import TmplanOperationPublicationInput
from .tmplan_table_publication_input import TmplanTablePublicationInput
from .traffic_regulation_publication_input import TrafficRegulationPublicationInput
from .vms_publication_input import VmsPublicationInput
from .vms_table_publication_input import VmsTablePublicationInput
from .warning_publication_input import WarningPublicationInput


@validataclass
class PayloadPublicationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    versionG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    modelBaseVersionG: str = StringValidator()
    extensionNameG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    extensionVersionG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    profileNameG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    profileVersionG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    afacOperatingHoursPublication: OperatingHoursPublicationInput | UnsetValueType = (
        DataclassValidator(OperatingHoursPublicationInput),
        Default(UnsetValue),
    )
    facRatesPublication: RatesPublicationInput | UnsetValueType = (
        DataclassValidator(RatesPublicationInput),
        Default(UnsetValue),
    )
    roaElaboratedDataPublication: ElaboratedDataPublicationInput | UnsetValueType = (
        DataclassValidator(ElaboratedDataPublicationInput),
        Default(UnsetValue),
    )
    roaMeasuredDataPublication: MeasuredDataPublicationInput | UnsetValueType = (
        DataclassValidator(MeasuredDataPublicationInput),
        Default(UnsetValue),
    )
    fstDevicePublication: DevicePublicationInput | UnsetValueType = (
        DataclassValidator(DevicePublicationInput),
        Default(UnsetValue),
    )
    czControlledZoneTablePublication: ControlledZoneTablePublicationInput | UnsetValueType = (
        DataclassValidator(ControlledZoneTablePublicationInput),
        Default(UnsetValue),
    )
    fstFaultPublication: FaultPublicationInput | UnsetValueType = (
        DataclassValidator(FaultPublicationInput),
        Default(UnsetValue),
    )
    troPredefinedConditionPublication: PredefinedConditionPublicationInput | UnsetValueType = (
        DataclassValidator(PredefinedConditionPublicationInput),
        Default(UnsetValue),
    )
    afacOrganisationPublication: OrganisationPublicationInput | UnsetValueType = (
        DataclassValidator(OrganisationPublicationInput),
        Default(UnsetValue),
    )
    roaMeasurementSiteTablePublication: MeasurementSiteTablePublicationInput | UnsetValueType = (
        DataclassValidator(MeasurementSiteTablePublicationInput),
        Default(UnsetValue),
    )
    czDynamicActivationStatusPublication: DynamicActivationStatusPublicationInput | UnsetValueType = (
        DataclassValidator(DynamicActivationStatusPublicationInput),
        Default(UnsetValue),
    )
    prkParkingTablePublication: ParkingTablePublicationInput | UnsetValueType = (
        DataclassValidator(ParkingTablePublicationInput),
        Default(UnsetValue),
    )
    egiEnergyInfrastructureStatusPublication: EnergyInfrastructureStatusPublicationInput | UnsetValueType = (
        DataclassValidator(EnergyInfrastructureStatusPublicationInput),
        Default(UnsetValue),
    )
    fstStatusPublication: StatusPublicationInput | UnsetValueType = (
        DataclassValidator(StatusPublicationInput),
        Default(UnsetValue),
    )
    egiEnergyInfrastructureTablePublication: EnergyInfrastructureTablePublicationInput | UnsetValueType = (
        DataclassValidator(EnergyInfrastructureTablePublicationInput),
        Default(UnsetValue),
    )
    tmpTmplanOperationPublication: TmplanOperationPublicationInput | UnsetValueType = (
        DataclassValidator(TmplanOperationPublicationInput),
        Default(UnsetValue),
    )
    aegiEnergyInfrastructureTablePublication: EnergyInfrastructureTablePublicationInput | UnsetValueType = (
        DataclassValidator(EnergyInfrastructureTablePublicationInput),
        Default(UnsetValue),
    )
    afacRatesPublication: RatesPublicationInput | UnsetValueType = (
        DataclassValidator(RatesPublicationInput),
        Default(UnsetValue),
    )
    troWarningPublication: WarningPublicationInput | UnsetValueType = (
        DataclassValidator(WarningPublicationInput),
        Default(UnsetValue),
    )
    facOperatingHoursPublication: OperatingHoursPublicationInput | UnsetValueType = (
        DataclassValidator(OperatingHoursPublicationInput),
        Default(UnsetValue),
    )
    facOrganisationPublication: OrganisationPublicationInput | UnsetValueType = (
        DataclassValidator(OrganisationPublicationInput),
        Default(UnsetValue),
    )
    vmsVmsPublication: VmsPublicationInput | UnsetValueType = (
        DataclassValidator(VmsPublicationInput),
        Default(UnsetValue),
    )
    vmsVmsTablePublication: VmsTablePublicationInput | UnsetValueType = (
        DataclassValidator(VmsTablePublicationInput),
        Default(UnsetValue),
    )
    aegiEnergyInfrastructureStatusPublication: EnergyInfrastructureStatusPublicationInput | UnsetValueType = (
        DataclassValidator(EnergyInfrastructureStatusPublicationInput),
        Default(UnsetValue),
    )
    locPredefinedLocationsPublication: PredefinedLocationsPublicationInput | UnsetValueType = (
        DataclassValidator(PredefinedLocationsPublicationInput),
        Default(UnsetValue),
    )
    prkParkingStatusPublication: ParkingStatusPublicationInput | UnsetValueType = (
        DataclassValidator(ParkingStatusPublicationInput),
        Default(UnsetValue),
    )
    sitSituationPublication: SituationPublicationInput | UnsetValueType = (
        DataclassValidator(SituationPublicationInput),
        Default(UnsetValue),
    )
    tmpTmplanTablePublication: TmplanTablePublicationInput | UnsetValueType = (
        DataclassValidator(TmplanTablePublicationInput),
        Default(UnsetValue),
    )
    comGenericPublication: GenericPublicationInput | UnsetValueType = (
        DataclassValidator(GenericPublicationInput),
        Default(UnsetValue),
    )
    troTrafficRegulationPublication: TrafficRegulationPublicationInput | UnsetValueType = (
        DataclassValidator(TrafficRegulationPublicationInput),
        Default(UnsetValue),
    )
