from datetime import datetime

from tap_titans.models.generic import Player, ClanCode
from tap_titans.models.model_type import TargetStateParts, TargetStates, EnemyIDs
from tap_titans.utils.base import Struct


class RaidTargetTitanState(Struct):
    id: TargetStateParts
    state: TargetStates


class RaidTarget(Struct):
    clan_code: ClanCode
    raid_id: int
    enemy_id: EnemyIDs
    updated_at: datetime
    player: Player
    state: tuple[RaidTargetTitanState, ...]
