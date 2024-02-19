from tap_titans.models.player import Player
from tap_titans.models.code import ClanCode
from tap_titans.utils.base import BaseModel


class PlayerMorale(BaseModel):
    player: Player
    clan_code: ClanCode
    amount: int
