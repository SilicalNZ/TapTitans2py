from tap_titans.models.code import ClanCode
from tap_titans.utils.base import BaseModel


class Message(BaseModel):
    message: str


class ClanRemoved(BaseModel):
    clan_code: ClanCode
    namespace: str
