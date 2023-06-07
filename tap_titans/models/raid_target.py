from tap_titans.models.player import Player
from tap_titans.models.model_type import Enemy
from tap_titans.utils.base import BaseModel


class RaidTargetTitan(BaseModel):
    enemy_id: Enemy
    state: str


class RaidTarget(BaseModel):
    player: Player
    titan_target: RaidTargetTitan
