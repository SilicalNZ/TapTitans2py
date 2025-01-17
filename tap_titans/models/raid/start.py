from datetime import datetime

from tap_titans.models.generic import Player, ClanAddedRaidTarget, ClanCode, Raid, EnemyIDs, EnemyNames, TitanParts, TitanAreaTypes, TitanCurseTypes
from tap_titans.utils.base import Struct, field


class TitanAreaDebuff(Struct):
    bonus_type: TitanAreaTypes
    bonus_amount: float


class TitanCursedDebuff(Struct):
    bonus_type: TitanCurseTypes
    bonus_amount: float


class RaidStartRaidTitanPart(Struct):
    part_id: TitanParts
    total_hp: float
    current_hp: float
    cursed: bool = False


class RaidStartRaidTitan(Struct):
    enemy_name: EnemyNames
    enemy_id: EnemyIDs
    total_hp: float
    current_hp: float
    parts: tuple[RaidStartRaidTitanPart, ...]
    area_debuffs: tuple[TitanAreaDebuff, ...] = field(default_factory=tuple)
    cursed_debuffs: tuple[TitanCursedDebuff, ...] = field(default_factory=tuple)


class RaidStartRaidAreaBuff(Struct):
    bonus_type: str  # Change to enum when it is documented
    bonus_amount: float


class RaidStartRaidInfo(Raid):
    spawn_sequence: tuple[EnemyNames, ...]
    titans: tuple[RaidStartRaidTitan, ...]
    area_buffs: tuple[RaidStartRaidAreaBuff, ...] = field(default_factory=tuple)


class RaidStartMoraleBonus(Struct):
    bonus_type: str
    bonus_amount: float


class RaidStartMorale(Struct):
    bonus_amount: float
    used: int


class RaidStartClanAdded(Struct):
    clan_code: ClanCode
    raid_id: int
    keys_remaining: int
    morale: RaidStartMorale
    raid: RaidStartRaidInfo
    start_at: datetime
    titan_target: tuple[ClanAddedRaidTarget, ...]


class RaidStart(Struct):
    clan_code: ClanCode
    raid_id: int
    keys_remaining: int
    morale: RaidStartMorale
    raid: RaidStartRaidInfo
    start_at: datetime
    player: Player

