from datetime import datetime

from tap_titans.models import model_type
from tap_titans.models.player import Player
from tap_titans.models.code import ClanCode
from tap_titans.utils.base import BaseModel


class RaidAttackStart(BaseModel):
    cards: tuple[model_type.Card, ...]
    clan_code: ClanCode
    player: Player
    raid_id: int
    started_at: datetime
