from typing import NewType

from tap_titans.models.code import *
from tap_titans.models.model_type import *
from tap_titans.utils.base import Struct


class Player(Struct):
    name: str
    player_code: PlayerCode


class RaidMorale(Struct):
    bonus_amount: float
    used: int


class Raid(Struct):
    tier: int | str
    level: int | str


class Message(Struct):
    message: str


Card = NewType("Card", str)


class ClanAddedRaidTargetTitanState(Struct):
    id: TargetStateParts
    state: TargetStates


class ClanAddedRaidTarget(Struct):
    enemy_id: EnemyIDs
    state: tuple[ClanAddedRaidTargetTitanState, ...]
