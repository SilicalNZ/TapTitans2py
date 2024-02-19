from tap_titans.models.player import Player
from tap_titans.models.code import ClanCode
from tap_titans.utils.base import BaseModel


class ClanKick(BaseModel):
    clan_code: ClanCode
    player: Player
    executor: Player


class ClanLeave(BaseModel):
    clan_code: ClanCode
    player: Player


class ClanJoin(BaseModel):
    clan_code: ClanCode
    player: Player


class ClanSync(BaseModel):
    clan_code: ClanCode
    clan_name: str