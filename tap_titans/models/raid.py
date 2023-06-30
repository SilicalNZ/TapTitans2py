from tap_titans.utils.base import BaseModel


class Raid(BaseModel):
    tier: int | str
    level: int | str
