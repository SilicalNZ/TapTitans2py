from typing import Coroutine, Any

import socketio
from pydantic import validate_arguments

from tap_titans.models import models


API_URL = "https://tt2-public.gamehivegames.com/api/raid"


class WebsocketClient:
    def __init__(
            self,
            connected: Coroutine[None, None, None] = None,
            disconnected: Coroutine[None, None, None] = None,
            error: Coroutine[models.Message, None, None] = None,
            connection_error: Coroutine[models.Message, None, None] = None,
            revoked_connection: Coroutine[None, None, None] = None,
            raid_attack: Coroutine[models.RaidAttack, None, None] = None,
            raid_start: Coroutine[models.RaidStart, None, None] = None,
            raid_end: Coroutine[models.RaidEnd, None, None] = None,
            raid_retire: Coroutine[models.RaidRetire, None, None] = None,
            raid_cycle_reset: Coroutine[models.RaidCycleReset, None, None] = None,
            raid_target_changed: Coroutine[models.RaidTarget, None, None] = None,
    ):
        events: dict[models.Event, Any] = {
            models.Event.CONNECTED: connected,
            models.Event.DISCONNECTED: disconnected,
            models.Event.ERROR: error,
            models.Event.CONNECTION_ERROR: connection_error,
            models.Event.REVOKED_CONNECTION: revoked_connection,
            models.Event.RAID_ATTACK: raid_attack,
            models.Event.RAID_START: raid_start,
            models.Event.RAID_END: raid_end,
            models.Event.RAID_RETIRE: raid_retire,
            models.Event.RAID_CYCLE_RESET: raid_cycle_reset,
            models.Event.RAID_TARGET_CHANGED: raid_target_changed,
        }

        self.sio = socketio.AsyncClient()

        for key, value in events.items():
            if value is not None:
                self.sio.event(key)(validate_arguments(value))

    async def connect(self, auth: str):
        await self.sio.connect(API_URL, headers={"API-Authenticate": auth})
        await self.sio.wait()
