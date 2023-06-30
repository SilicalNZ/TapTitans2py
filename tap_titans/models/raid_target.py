from datetime import datetime

from tap_titans.models.player import Player
from tap_titans.models.model_type import TargetStatePart, TargetState
from tap_titans.models.code import ClanCode
from tap_titans.utils.base import BaseModel


class RaidTargetTitanState(BaseModel):
    id: TargetStatePart
    state: TargetState


class RaidTarget(BaseModel):
    clan_code: ClanCode
    raid_id: int
    updated_at: datetime
    player: Player
    state: tuple[RaidTargetTitanState, ...]
