from tap_titans.models.code import PlayerCode
from tap_titans.utils.base import BaseModel


class Raid(BaseModel):
    tier: int
    level: int
