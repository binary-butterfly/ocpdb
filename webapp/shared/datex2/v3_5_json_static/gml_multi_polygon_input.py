"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .gml_polygon_input import GmlPolygonInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class GmlMultiPolygonInput(ValidataclassMixin):
    """
    An area defined by a set of polygons acording to GML (EN ISO 19136).
    """

    gmlAreaName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    gmlPolygon: list[GmlPolygonInput] = ListValidator(DataclassValidator(GmlPolygonInput))
    locGmlMultiPolygonExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
