from tap_titans.models.generic import Player, OptionalPlayer, ClanCode
from tap_titans.utils.base import Struct


class ClanKick(Struct):
    clan_code: ClanCode
    player: Player
    executor: OptionalPlayer
