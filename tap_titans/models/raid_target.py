from tap_titans.models.player import Player
from tap_titans.models.model_type import Enemy
from tap_titans.models.model_type import TargetStatePart, TargetState
from tap_titans.utils.base import BaseModel


class RaidTargetTitanState(BaseModel):
    id: TargetStatePart
    state: TargetState


class RaidTargetTitan(BaseModel):
    enemy_id: Enemy
    state: tuple[RaidTargetTitanState, ...]


class RaidTarget(BaseModel):
    raid_id: int
    player: Player
    titan_target: tuple[RaidTargetTitan, ...]
