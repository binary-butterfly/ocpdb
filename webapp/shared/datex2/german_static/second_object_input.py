"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .third_object_input import ThirdObjectInput


@dataclass(kw_only=True)
class SecondObjectInput:
    ThirdObject: ThirdObjectInput | None = None
    second_string: str | None = None
