from tap_titans.models.generic import TitanParts, PlayerCode, EnemyIDs
from tap_titans.utils.base import Struct


class DamageLog(Struct):
    id: TitanParts
    value: int


class Log(Struct):
    enemy_id: EnemyIDs
    titan_index: int
    damage_log: tuple[DamageLog, ...]


class RaidSummary(Struct):
    player_code: PlayerCode
    name: str
    num_attacks: int
    total_damage: int
    log: tuple[Log, ...]
