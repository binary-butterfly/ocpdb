"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class LoadTypeEnum(Enum):
    ABNORMALLOAD = 'abnormalLoad'
    AMMUNITION = 'ammunition'
    CHEMICALS = 'chemicals'
    COMBUSTIBLEMATERIALS = 'combustibleMaterials'
    CORROSIVEMATERIALS = 'corrosiveMaterials'
    DEBRIS = 'debris'
    EMPTY = 'empty'
    EXPLOSIVEMATERIALS = 'explosiveMaterials'
    EXTRAHIGHLOAD = 'extraHighLoad'
    EXTRALONGLOAD = 'extraLongLoad'
    EXTRAWIDELOAD = 'extraWideLoad'
    FUEL = 'fuel'
    GLASS = 'glass'
    GOODS = 'goods'
    HAZARDOUSMATERIALS = 'hazardousMaterials'
    LIQUID = 'liquid'
    LIVESTOCK = 'livestock'
    MATERIALS = 'materials'
    MATERIALSDANGEROUSFORPEOPLE = 'materialsDangerousForPeople'
    MATERIALSDANGEROUSFORTHEENVIRONMENT = 'materialsDangerousForTheEnvironment'
    MATERIALSDANGEROUSFORWATER = 'materialsDangerousForWater'
    OIL = 'oil'
    ORDINARY = 'ordinary'
    PERISHABLEPRODUCTS = 'perishableProducts'
    PETROL = 'petrol'
    PHARMACEUTICALMATERIALS = 'pharmaceuticalMaterials'
    RADIOACTIVEMATERIALS = 'radioactiveMaterials'
    REFRIGERATEDGOODS = 'refrigeratedGoods'
    REFUSE = 'refuse'
    TOXICMATERIALS = 'toxicMaterials'
    VEHICLES = 'vehicles'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
