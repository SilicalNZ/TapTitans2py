from datetime import datetime

from tap_titans.models.raid_summary import RaidSummary
from tap_titans.models.generic import PlayerCode, ClanCode
from tap_titans.utils.base import Struct


class RaidRetirePlayer(Struct):
    name: str | None = None
    player_code: PlayerCode | None = None


class RaidRetire(Struct):
    clan_code: ClanCode
    raid_id: int
    retired_at: datetime
    player: RaidRetirePlayer
    keys_remaining: int
    raid_summary: tuple[RaidSummary, ...]
