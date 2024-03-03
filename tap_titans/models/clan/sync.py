from tap_titans.models.generic import Player, ClanCode
from tap_titans.utils.base import Struct


class ClanSync(Struct):
    clan_code: ClanCode
    clan_name: str
