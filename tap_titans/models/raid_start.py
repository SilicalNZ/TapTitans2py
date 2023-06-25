from datetime import datetime
from typing import Optional

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
    cursed: bool


class RaidStartRaidTitan(BaseModel):
    enemy_name: model_type.EnemyName
    enemy_id: model_type.Enemy
    total_hp: int
    parts: tuple[RaidStartRaidTitanPart, ...]
    area_debuffs: tuple[TitanAreaDebuff, ...]
    cursed_debuffs: tuple[TitanCursedDebuff, ...]


class RaidStartRaidAreaBuff(BaseModel):
    bonus_type: str  # Change to enum when it is documented
    bonus_amount: float


class RaidStartRaid(Raid):
    spawn_sequence: tuple[model_type.EnemyName, ...]
    titans: tuple[RaidStartRaidTitan, ...]
    area_buffs: tuple[RaidStartRaidAreaBuff, ...]


class RaidStartMoraleBonus(BaseModel):
    # Tidy this up when it is fixed
    _BonusType: Optional[str] = Field(default=None, alias="BonusType")
    _BonusAmount: Optional[int] = Field(default=None, alias="BonusAmount")
    _bonus_type: Optional[str] = Field(default=None, alias="bonus_type")  # Change to enum when it is documented
    _bonus_amount: Optional[int] = Field(default=None, alias="bonus_amount")

    @property
    def bonus_type(self) -> str:
        return self._BonusType or self._bonus_type

    @property
    def bonus_amount(self) -> int:
        return self._BonusAmount or self._bonus_amount


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
