from datetime import datetime

from tap_titans.models.model_type import CardBonus
from tap_titans.models.code import ClanCode
from tap_titans.models.raid import Raid
from tap_titans.utils.base import BaseModel


class RaidCycleResetCardBonus(BaseModel):
    id: CardBonus
    value: int


class RaidCycleReset(BaseModel):
    clan_code: ClanCode
    raid_id: int
    raid: Raid
    next_reset_at: datetime
    card_bonuses: tuple[RaidCycleResetCardBonus, ...]
