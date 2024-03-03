from tap_titans.models.generic import Player, ClanCode
from tap_titans.utils.base import Struct


class ClanLeave(Struct):
    clan_code: ClanCode
    player: Player
