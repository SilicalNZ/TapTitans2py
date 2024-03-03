from datetime import datetime

from tap_titans.models.raid_summary import RaidSummary
from tap_titans.models.generic import ClanCode, RaidID
from tap_titans.utils.base import Struct


class RaidEnd(Struct):
    clan_code: ClanCode
    raid_id: RaidID
    ended_at: datetime
    keys_remaining: int
    raid_summary: tuple[RaidSummary, ...]
