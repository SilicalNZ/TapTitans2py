from tap_titans.models.code import PlayerCode
from tap_titans.utils.base import BaseModel


class Player(BaseModel):
    name: str
    player_code: PlayerCode
