from datetime import datetime

from tap_titans.models import model_type
from tap_titans.models.player import Player
from tap_titans.models.code import ClanCode
from tap_titans.models.raid import Raid
from tap_titans.utils.base import BaseModel


class RaidStartRaidTitanPart(BaseModel):
    part_id: model_type.TitanPart
    total_hp: int


class RaidStartRaidTitan(BaseModel):
    enemy_name: model_type.EnemyName
    enemy_id: model_type.Enemy
    total_hp: int
    parts: tuple[
        RaidStartRaidTitanPart,
        RaidStartRaidTitanPart,
        RaidStartRaidTitanPart,
        RaidStartRaidTitanPart,
        RaidStartRaidTitanPart,
        RaidStartRaidTitanPart,
        RaidStartRaidTitanPart,
        RaidStartRaidTitanPart,
    ]  # [8]RaidStartRaidTitanPart


class RaidStartRaid(Raid):
    spawn_sequence: tuple[model_type.EnemyName, ...]
    titans: tuple[RaidStartRaidTitan, ...]


class RaidStartMoraleBonus(BaseModel):
    BonusType: str
    BonusAmount: int


class RaidStartMorale(BaseModel):
    bonus: RaidStartMoraleBonus
    used: int


class RaidStart(BaseModel):
    clan_code: ClanCode
    raid_id: int
    player: Player
    keys_remaining: int
    morale: RaidStartMorale
    raid: RaidStartRaid
    start_at: datetime
