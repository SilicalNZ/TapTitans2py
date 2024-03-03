from datetime import datetime

from tap_titans.models.generic import Player, ClanCode, Card
from tap_titans.utils.base import Struct


class RaidAttackStart(Struct):
    cards: tuple[Card, ...]
    clan_code: ClanCode
    player: Player
    raid_id: int
    started_at: datetime
