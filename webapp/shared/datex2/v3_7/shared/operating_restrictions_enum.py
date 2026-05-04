"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class OperatingRestrictionsEnum(Enum):
    CARPOOLONLY = 'carpoolOnly'
    COMMERCIALVEHICLEONLY = 'commercialVehicleOnly'
    FREEPARKING = 'freeParking'
    BUSONLY = 'busOnly'
    BUSSTOP = 'busStop'
    DISABLEDPERSONPERMITONLY = 'disabledPersonPermitOnly'
    ELECTRICVEHICLEONLY = 'electricVehicleOnly'
    GOVERNMENTVEHICLEONLY = 'governmentVehicleOnly'
    LOADINGZONE = 'loadingZone'
    LOADINGZONECOMMERCIAL = 'loadingZoneCommercial'
    MEDIA = 'media'
    RESIDENTIALPERMITONLY = 'residentialPermitOnly'
    SNOW = 'snow'
    STREETCLEANING = 'streetCleaning'
    PARKINGTIMELIMIT = 'parkingTimeLimit'
    TAXIONLY = 'taxiOnly'
    VALETONLY = 'valetOnly'
    NOPARKING = 'noParking'
    NOWAITING = 'noWaiting'
    TEMPORARYPARKING = 'temporaryParking'
    EXTENDEDG = 'extendedG'
