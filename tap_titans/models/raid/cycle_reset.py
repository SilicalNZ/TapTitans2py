from datetime import datetime

from tap_titans.models.generic import RaidMorale, ClanCode, RaidID, CardBonuses
from tap_titans.utils.base import Struct


class RaidCycleResetCardBonus(Struct):
    id: CardBonuses
    value: float


class RaidCycleReset(Struct):
    clan_code: ClanCode
    raid_id: RaidID
    morale: RaidMorale
    raid_started_at: datetime
    next_reset_at: datetime
    card_bonuses: tuple[RaidCycleResetCardBonus, ...]
