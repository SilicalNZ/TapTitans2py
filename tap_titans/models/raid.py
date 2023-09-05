from tap_titans.utils.base import BaseModel


class RaidMorale(BaseModel):
    bonus_amount: float
    used: int


class Raid(BaseModel):
    tier: int | str
    level: int | str
