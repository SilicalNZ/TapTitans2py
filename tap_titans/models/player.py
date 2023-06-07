from tap_titans.models.code import ClanCode
from tap_titans.utils.base import BaseModel


class Player(BaseModel):
    name: str
    code: ClanCode
