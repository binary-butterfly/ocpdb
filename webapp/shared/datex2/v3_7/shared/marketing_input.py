"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .image_album_input import ImageAlbumInput


@validataclass
class MarketingInput(ValidataclassMixin):
    webUrl: list[str] | UnsetValueType = ListValidator(StringValidator()), Default(UnsetValue)
    imageAlbum: list[ImageAlbumInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ImageAlbumInput)),
        Default(UnsetValue),
    )
    prkMarketingExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
