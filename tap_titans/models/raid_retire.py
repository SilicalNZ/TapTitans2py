from datetime import datetime

from tap_titans.models.raid_summary import RaidSummary
from tap_titans.models.player import Player
from tap_titans.models.code import ClanCode
from tap_titans.utils.base import BaseModel


class RaidRetire(BaseModel):
    clan_code: ClanCode
    raid_id: int
    retired_at: datetime
    player: Player
    keys_remaining: int
    raid_summary: RaidSummary.S
