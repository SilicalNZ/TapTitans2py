from uuid import UUID

from tap_titans.models.generic import ClanCode
from tap_titans.utils.base import Struct


class ClanRemoved(Struct):
    clan_code: ClanCode
    namespace: str
    token: UUID
