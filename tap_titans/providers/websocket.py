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
            raid_attack_start: Callable[[models.RaidAttackStart], _empty_coro] | None = None,
            raid_attack: Callable[[models.RaidAttack], _empty_coro] | None = None,
            raid_start: Callable[[models.RaidStart], _empty_coro] | None = None,
            clan_added_raid_start: Callable[[models.ClanAddedRaidTarget], _empty_coro] | None = None,
            raid_end: Callable[[models.RaidEnd], _empty_coro] | None = None,
            raid_retire: Callable[[models.RaidRetire], _empty_coro] | None = None,
            raid_cycle_reset: Callable[[models.RaidCycleReset], _empty_coro] | None = None,
            clan_added_cycle: Callable[[models.ClanAddedRaidCycleReset], _empty_coro] | None = None,
            raid_target_changed: Callable[[models.RaidTarget], _empty_coro] | None = None,
            clan_join: Callable[[models.ClanJoin], _empty_coro] | None = None,
            clan_leave: Callable[[models.ClanLeave], _empty_coro] | None = None,
            clan_kick: Callable[[models.ClanKick], _empty_coro] | None = None,
            clan_sync: Callable[[models.ClanSync], _empty_coro] | None = None,
            player_morale: Callable[[models.PlayerMorale], _empty_coro] | None = None,
            setting_validate_arguments: bool = True,
            player_connected: Callable[[], _empty_coro] | None = None,
            player_disconnected: Callable[[], _empty_coro] | None = None,
            player_error: Callable[[models.Message], _empty_coro] | None = None,
            player_connection_error: Callable[[models.Message], _empty_coro] | None = None,
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

        clan_events: dict[models.ClanEvent, Any] = {
            models.ClanEvent.CONNECTED: connected,
            models.ClanEvent.DISCONNECTED: disconnected,
            models.ClanEvent.ERROR: _converter(error, models.Message),
            models.ClanEvent.CONNECTION_ERROR: _converter(connection_error, models.Message),
            models.ClanEvent.CLAN_REMOVED: _converter(clan_removed, models.ClanRemoved),
            models.ClanEvent.RAID_ATTACK_START: _converter(raid_attack_start, models.RaidAttackStart),
            models.ClanEvent.RAID_ATTACK: _converter(raid_attack, models.RaidAttack),
            models.ClanEvent.RAID_START: _converter(raid_start, models.RaidStart),
            models.ClanEvent.CLAN_ADDED_RAID_START: _converter(clan_added_raid_start, models.RaidStart),
            models.ClanEvent.RAID_END: _converter(raid_end, models.RaidEnd),
            models.ClanEvent.RAID_RETIRE: _converter(raid_retire, models.RaidRetire),
            models.ClanEvent.RAID_CYCLE_RESET: _converter(raid_cycle_reset, models.RaidCycleReset),
            models.ClanEvent.CLAN_ADDED_CYCLE: _converter(clan_added_cycle, models.ClanAddedRaidCycleReset),
            models.ClanEvent.RAID_TARGET_CHANGED: _converter(raid_target_changed, models.RaidTarget),
            models.ClanEvent.CLAN_JOIN: _converter(clan_join, models.ClanJoin),
            models.ClanEvent.CLAN_LEAVE: _converter(clan_leave, models.ClanLeave),
            models.ClanEvent.CLAN_KICK: _converter(clan_kick, models.ClanKick),
            models.ClanEvent.CLAN_SYNC: _converter(clan_sync, models.ClanSync),
            models.ClanEvent.PLAYER_MORALE: _converter(player_morale, models.PlayerMorale),
        }

        player_events: dict[models.PlayerEvent, Any] = {
            models.PlayerEvent.CONNECTED: player_connected,
            models.PlayerEvent.DISCONNECTED: player_disconnected,
            models.PlayerEvent.ERROR: _converter(player_error, models.Message),
            models.PlayerEvent.CONNECTION_ERROR: _converter(player_connection_error, models.Message),
        }

        self.sio = socketio.AsyncClient()

        for key, value in clan_events.items():
            if value is not None:
                self.sio.on(key.value, namespace="/raid")(value)

        for key, value in player_events.items():
            if value is not None:
                self.sio.on(key.value, namespace="/player")(value)

    async def connect(self, auth: str):
        await self.sio.connect(
            API_URL,
            transports=["websocket"],
            headers={"API-Authenticate": auth},
            socketio_path="api",
            namespaces=["/raid", "/player"],
        )
        await self.sio.wait()
