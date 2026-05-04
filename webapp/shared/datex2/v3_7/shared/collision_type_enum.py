"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class CollisionTypeEnum(Enum):
    COLLISIONWITHANIMAL = 'collisionWithAnimal'
    COLLISIONWITHOBSTACLE = 'collisionWithObstacle'
    COLLISIONWITHPERSON = 'collisionWithPerson'
    HEADONCOLLISION = 'headOnCollision'
    HEADONORSIDECOLLISION = 'headOnOrSideCollision'
    MULTIPLEVEHICLECOLLISION = 'multipleVehicleCollision'
    REARCOLLISION = 'rearCollision'
    SIDECOLLISION = 'sideCollision'
    EXTENDEDG = 'extendedG'
