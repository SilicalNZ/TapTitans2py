from datetime import datetime

from tap_titans.models.generic import Player, ClanCode, RaidID, TitanParts, EnemyIDs, Card
from tap_titans.utils.base import Struct


class RaidAttackEndRaidStateCurrentPart(Struct):
    part_id: TitanParts
    current_hp: int


class RaidAttackEndRaidStateCurrent(Struct):
    current_hp: int
    enemy_id: EnemyIDs
    parts: tuple[RaidAttackEndRaidStateCurrentPart, ...]


class RaidAttackEndRaidState(Struct):
    titan_index: int
    current: RaidAttackEndRaidStateCurrent


class RaidAttackEndCardLevel(Struct):
    id: Card
    value: int


class RaidAttackEndCardDamageLog(Struct):
    id: TitanParts
    value: int


class RaidAttackEndCardDamage(Struct):
    titan_index: int
    id: Card | None
    damage_log: tuple[RaidAttackEndCardDamageLog, ...]


class RaidAttackEndLog(Struct):
    cards_damage: tuple[RaidAttackEndCardDamage, ...]
    cards_level: tuple[RaidAttackEndCardLevel, ...]
    attack_datetime: datetime


class RaidAttackEndPlayer(Player):
    raid_level: int
    attacks_remaining: int


class RaidAttackEnd(Struct):
    clan_code: ClanCode
    raid_id: RaidID
    cycle: int
    player: RaidAttackEndPlayer
    attack_log: RaidAttackEndLog
    raid_state: RaidAttackEndRaidState
