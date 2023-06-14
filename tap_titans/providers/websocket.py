from typing import Coroutine, Any

import socketio
from pydantic import validate_arguments

from tap_titans.models import models


API_URL = "wss://tt2-public.gamehivegames.com"


class WebsocketClient:
    def __init__(
            self,
            connected: Coroutine[None, None, None] = None,
            disconnected: Coroutine[None, None, None] = None,
            error: Coroutine[models.Message, None, None] = None,
            connection_error: Coroutine[models.Message, None, None] = None,
            clan_removed: Coroutine[None, None, None] = None,
            raid_attack: Coroutine[models.RaidAttack, None, None] = None,
            raid_start: Coroutine[models.RaidStart, None, None] = None,
            clan_added_raid_start: Coroutine[models.RaidStart, None, None] = None,
            raid_end: Coroutine[models.RaidEnd, None, None] = None,
            raid_retire: Coroutine[models.RaidRetire, None, None] = None,
            raid_cycle_reset: Coroutine[models.RaidCycleReset, None, None] = None,
            clan_added_cycle: Coroutine[models.RaidCycleReset, None, None] = None,
            raid_target_changed: Coroutine[models.RaidTarget, None, None] = None,
            setting_validate_arguments: bool = True,
    ):
        events: dict[models.Event, Any] = {
            models.Event.CONNECTED: connected,
            models.Event.DISCONNECTED: disconnected,
            models.Event.ERROR: error,
            models.Event.CONNECTION_ERROR: connection_error,
            models.Event.CLAN_REMOVED: clan_removed,
            models.Event.RAID_ATTACK: raid_attack,
            models.Event.RAID_START: raid_start,
            models.Event.CLAN_ADDED_RAID_START: clan_added_raid_start,
            models.Event.RAID_END: raid_end,
            models.Event.RAID_RETIRE: raid_retire,
            models.Event.RAID_CYCLE_RESET: raid_cycle_reset,
            models.Event.CLAN_ADDED_CYCLE: clan_added_cycle,
            models.Event.RAID_TARGET_CHANGED: raid_target_changed,
        }

        self.sio = socketio.AsyncClient()

        for key, value in events.items():
            if value is not None:
                self.sio.on(key.value, namespace="/raid")(validate_arguments(value) if setting_validate_arguments else value)

    async def connect(self, auth: str):
        await self.sio.connect(
            API_URL,
            transports=["websocket"],
            headers={"API-Authenticate": auth},
            socketio_path="api",
            namespaces=["/raid"],
        )
        await self.sio.wait()
