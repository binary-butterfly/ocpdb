"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .second_object_input import SecondObjectInput


@dataclass(kw_only=True)
class SimpleSchemaInput:
    SecondObject: SecondObjectInput | None = None
