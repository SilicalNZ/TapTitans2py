from datetime import datetime

from tap_titans.models.raid.start import RaidStartRaidInfo
from tap_titans.models.generic import CardBonuses, ClanAddedRaidTarget, RaidMorale, RaidID, ClanCode
from tap_titans.utils.base import Struct


class RaidCycleResetCardBonus(Struct):
    id: CardBonuses
    value: float


class RaidCycleResetClanAdded(Struct):
    clan_code: ClanCode
    raid_id: RaidID
    morale: RaidMorale
    raid: RaidStartRaidInfo
    titan_target: tuple[ClanAddedRaidTarget, ...]
    raid_started_at: datetime
    next_reset_at: datetime
    card_bonuses: tuple[RaidCycleResetCardBonus, ...]
