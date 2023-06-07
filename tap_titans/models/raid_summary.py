from tap_titans.models import model_type
from tap_titans.models.code import RaidSummaryCode
from tap_titans.utils.base import BaseModel


class DamageLog(BaseModel):
    id: model_type.TitanPart
    value: int


class Log(BaseModel):
    enemy_id: model_type.Enemy
    titan_index: int
    damage_log: tuple[DamageLog, ...]


class RaidSummary(BaseModel):
    S = tuple['RaidSummary', ...]

    code: RaidSummaryCode
    log: tuple[Log, ...]




