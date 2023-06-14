from datetime import datetime

from tap_titans.models.raid_summary import RaidSummary
from tap_titans.models.code import ClanCode
from tap_titans.utils.base import BaseModel


class RaidEnd(BaseModel):
    clan_code: ClanCode
    raid_id: int
    ended_at: datetime
    keys_remaining: int
    raid_summary: RaidSummary.S
