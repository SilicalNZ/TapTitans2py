from datetime import datetime

from tap_titans.models.raid_summary import RaidSummary
from tap_titans.models.generic import Player, ClanCode
from tap_titans.utils.base import Struct


class RaidRetire(Struct):
    clan_code: ClanCode
    raid_id: int
    retired_at: datetime
    player: Player
    keys_remaining: int
    raid_summary: tuple[RaidSummary, ...]
