from datetime import datetime

from tap_titans.models.model_type import CardBonus
from tap_titans.models.code import ClanCode
from tap_titans.models.raid_start import RaidStartRaid
from tap_titans.utils.base import BaseModel


class RaidCycleResetCardBonus(BaseModel):
    id: CardBonus
    value: int


class ClanAddedRaidCycleReset(BaseModel):
    clan_code: ClanCode
    raid_id: int
    raid: RaidStartRaid
    next_reset_at: datetime
    card_bonuses: tuple[RaidCycleResetCardBonus, ...]
