from tap_titans.models.generic import Player, ClanCode
from tap_titans.utils.base import Struct


class PlayerMorale(Struct):
    player: Player
    clan_code: ClanCode
    amount: int
