from datetime import datetime

from pydantic import Field

from tap_titans.models import model_type
from tap_titans.models.player import Player
from tap_titans.models.code import ClanCode
from tap_titans.models.raid import Raid
from tap_titans.utils.base import BaseModel


class TitanAreaDebuff(BaseModel):
    bonus_type: str  # Change to enum when it is documented
    bonus_amount: float


class TitanCursedDebuff(BaseModel):
    bonus_type: str  # Change to enum when it is documented
    bonus_amount: float


class RaidStartRaidTitanPart(BaseModel):
    part_id: model_type.TitanPart
    total_hp: int
    cursed: bool = Field(default=False, alias="cursed")


class RaidStartRaidTitan(BaseModel):
    enemy_name: model_type.EnemyName
    enemy_id: model_type.Enemy
    total_hp: int
    parts: tuple[RaidStartRaidTitanPart, ...]
    area_debuffs: tuple[TitanAreaDebuff, ...]
    cursed_debuffs: tuple[TitanCursedDebuff, ...] = Field(default=())


class RaidStartRaidAreaBuff(BaseModel):
    bonus_type: str  # Change to enum when it is documented
    bonus_amount: float


class RaidStartRaid(Raid):
    spawn_sequence: tuple[model_type.EnemyName, ...]
    titans: tuple[RaidStartRaidTitan, ...]
    area_buffs: tuple[RaidStartRaidAreaBuff, ...]


class RaidStartMoraleBonus(BaseModel):
    bonus_type: str
    bonus_amount: float


class RaidStartMorale(BaseModel):
    bonus_amount: float
    used: int

    # Compatibility <6.2
    @property
    def bonus(self) -> RaidStartMoraleBonus:
        return RaidStartMoraleBonus(
            bonus_type="AllRaidDamage",
            bonus_amount=self.bonus_amount,
        )


class RaidSubStart(BaseModel):
    clan_code: ClanCode
    raid_id: int
    keys_remaining: int
    morale: RaidStartMorale
    raid: RaidStartRaid
    start_at: datetime


class RaidStart(RaidSubStart):
    player: Player
