from datetime import datetime

from tap_titans.models.model_type import CardBonus
from tap_titans.models.raid import RaidMorale
from tap_titans.models.code import ClanCode
from tap_titans.utils.base import BaseModel


class RaidCycleResetCardBonus(BaseModel):
    id: CardBonus
    value: float


class RaidCycleReset(BaseModel):
    clan_code: ClanCode
    raid_id: int
    morale: RaidMorale
    raid_started_at: datetime
    next_reset_at: datetime
    card_bonuses: tuple[RaidCycleResetCardBonus, ...]
