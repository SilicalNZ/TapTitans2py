from typing import Coroutine, Any, Callable

import socketio

from tap_titans.models import models


API_URL = "wss://tt2-public.gamehivegames.com"

_empty_coro = Coroutine[None, None, None]


class WebsocketClient:
    def __init__(
            self,
            connected: Callable[[], _empty_coro] | None = None,
            disconnected: Callable[[], _empty_coro] | None = None,
            error: Callable[[models.Message], _empty_coro] | None = None,
            connection_error: Callable[[models.Message], _empty_coro] | None = None,
            clan_removed: Callable[[models.ClanRemoved], _empty_coro] | None = None,
            raid_attack: Callable[[models.RaidAttack], _empty_coro] | None = None,
            raid_start: Callable[[models.RaidStart], _empty_coro] | None = None,
            clan_added_raid_start: Callable[[models.RaidStart], _empty_coro] | None = None,
            raid_end: Callable[[models.RaidEnd], _empty_coro] | None = None,
            raid_retire: Callable[[models.RaidRetire], _empty_coro] | None = None,
            raid_cycle_reset: Callable[[models.RaidCycleReset], _empty_coro] | None = None,
            clan_added_cycle: Callable[[models.ClanAddedRaidCycleReset], _empty_coro] | None = None,
            raid_target_changed: Callable[[models.RaidTarget], _empty_coro] | None = None,
            setting_validate_arguments: bool = True,
            **kwargs,
    ):
        def _converter(func, convert_to):
            if func is None:
                return None

            # Included this for backwards compatibility. Some users may be asking for a dict
            if not setting_validate_arguments:
                return func

            async def __wrapper(arg: dict):
                await func(convert_to(**arg))

            return __wrapper

        events: dict[models.Event, Any] = {
            models.Event.CONNECTED: connected,
            models.Event.DISCONNECTED: disconnected,
            models.Event.ERROR: _converter(error, models.Message),
            models.Event.CONNECTION_ERROR: _converter(connection_error, models.Message),
            models.Event.CLAN_REMOVED: _converter(clan_removed, models.ClanRemoved),
            models.Event.RAID_ATTACK: _converter(raid_attack, models.RaidAttack),
            models.Event.RAID_START: _converter(raid_start, models.RaidStart),
            models.Event.CLAN_ADDED_RAID_START: _converter(clan_added_raid_start, models.RaidStart),
            models.Event.RAID_END: _converter(raid_end, models.RaidEnd),
            models.Event.RAID_RETIRE: _converter(raid_retire, models.RaidRetire),
            models.Event.RAID_CYCLE_RESET: _converter(raid_cycle_reset, models.RaidCycleReset),
            models.Event.CLAN_ADDED_CYCLE: _converter(clan_added_cycle, models.ClanAddedRaidCycleReset),
            models.Event.RAID_TARGET_CHANGED: _converter(raid_target_changed, models.RaidTarget),
        }

        self.sio = socketio.AsyncClient()

        for key, value in events.items():
            if value is not None:
                self.sio.on(key.value, namespace="/raid")(value)

    async def connect(self, auth: str):
        await self.sio.connect(
            API_URL,
            transports=["websocket"],
            headers={"API-Authenticate": auth},
            socketio_path="api",
            namespaces=["/raid"],
        )
        await self.sio.wait()
