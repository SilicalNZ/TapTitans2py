from typing import Coroutine, Any, Callable

import socketio

from tap_titans.models import models
from tap_titans.utils.base import Struct


API_URL = "wss://tt2-public.gamehivegames.com"

_empty_coro = Coroutine[None, None, None]


class WebsocketClient:
    def __init__(
            self,
            connected: Callable[[], _empty_coro] | None = None,
            disconnected: Callable[[], _empty_coro] | None = None,
            error: Callable[[models.Message | dict], _empty_coro] | None = None,
            connection_error: Callable[[models.Message | dict], _empty_coro] | None = None,
            clan_removed: Callable[[models.clan_models.ClanRemoved | dict], _empty_coro] | None = None,
            raid_attack_start: Callable[[models.raid_models.RaidAttackStart | dict], _empty_coro] | None = None,
            raid_attack_end: Callable[[models.raid_models.RaidAttackEnd | dict], _empty_coro] | None = None,
            raid_start: Callable[[models.raid_models.RaidStart | dict], _empty_coro] | None = None,
            clan_added_raid_start: Callable[[models.raid_models.RaidStartClanAdded | dict], _empty_coro] | None = None,
            raid_end: Callable[[models.raid_models.RaidEnd | dict], _empty_coro] | None = None,
            raid_retire: Callable[[models.raid_models.RaidRetire | dict], _empty_coro] | None = None,
            raid_cycle_reset: Callable[[models.raid_models.RaidCycleReset | dict], _empty_coro] | None = None,
            clan_added_cycle: Callable[[models.raid_models.RaidCycleResetClanAdded | dict], _empty_coro] | None = None,
            raid_target_changed: Callable[[models.raid_models.RaidTarget | dict], _empty_coro] | None = None,
            clan_join: Callable[[models.clan_models.ClanJoin | dict], _empty_coro] | None = None,
            clan_leave: Callable[[models.clan_models.ClanLeave | dict], _empty_coro] | None = None,
            clan_kick: Callable[[models.clan_models.ClanKick | dict], _empty_coro] | None = None,
            clan_sync: Callable[[models.clan_models.ClanSync | dict], _empty_coro] | None = None,
            player_morale: Callable[[models.clan_models.PlayerMorale | dict], _empty_coro] | None = None,
            setting_validate_arguments: bool = True,
            player_connected: Callable[[], _empty_coro] | None = None,
            player_disconnected: Callable[[], _empty_coro] | None = None,
            player_error: Callable[[models.Message | dict], _empty_coro] | None = None,
            player_connection_error: Callable[[models.Message | dict], _empty_coro] | None = None,
    ):
        def _converter(func, convert_to: type[Struct] | dict):
            if func is None:
                return None

            # Some users may be asking for a dict
            if not setting_validate_arguments:
                return func

            async def __wrapper(arg: dict):
                try:
                    await func(convert_to.decode_dict(arg))
                except Exception as e:
                    raise ValueError(f"{func.__name__} failed to be called") from e

            return __wrapper

        clan_events: dict[models.ClanEvents, Any] = {
            models.ClanEvents.CONNECTED: connected,
            models.ClanEvents.DISCONNECTED: disconnected,
            models.ClanEvents.ERROR: _converter(error, models.Message),
            models.ClanEvents.CONNECTION_ERROR: _converter(connection_error, models.Message),
            models.ClanEvents.CLAN_REMOVED: _converter(clan_removed, models.clan_models.ClanRemoved),
            models.ClanEvents.RAID_ATTACK_START: _converter(raid_attack_start, models.raid_models.RaidAttackStart),
            models.ClanEvents.RAID_ATTACK_END: _converter(raid_attack_end, models.raid_models.RaidAttackEnd),
            models.ClanEvents.RAID_START: _converter(raid_start, models.raid_models.RaidStart),
            models.ClanEvents.CLAN_ADDED_RAID_START: _converter(clan_added_raid_start, models.raid_models.RaidStartClanAdded),
            models.ClanEvents.RAID_END: _converter(raid_end, models.raid_models.RaidEnd),
            models.ClanEvents.RAID_RETIRE: _converter(raid_retire, models.raid_models.RaidRetire),
            models.ClanEvents.RAID_CYCLE_RESET: _converter(raid_cycle_reset, models.raid_models.RaidCycleReset),
            models.ClanEvents.CLAN_ADDED_CYCLE: _converter(clan_added_cycle, models.raid_models.RaidCycleResetClanAdded),
            models.ClanEvents.RAID_TARGET_CHANGED: _converter(raid_target_changed, models.raid_models.RaidTarget),
            models.ClanEvents.CLAN_JOIN: _converter(clan_join, models.clan_models.ClanJoin),
            models.ClanEvents.CLAN_LEAVE: _converter(clan_leave, models.clan_models.ClanLeave),
            models.ClanEvents.CLAN_KICK: _converter(clan_kick, models.clan_models.ClanKick),
            models.ClanEvents.CLAN_SYNC: _converter(clan_sync, models.clan_models.ClanSync),
            models.ClanEvents.PLAYER_MORALE: _converter(player_morale, models.clan_models.PlayerMorale),
        }

        player_events: dict[models.PlayerEvents, Any] = {
            models.PlayerEvents.CONNECTED: player_connected,
            models.PlayerEvents.DISCONNECTED: player_disconnected,
            models.PlayerEvents.ERROR: _converter(player_error, models.Message),
            models.PlayerEvents.CONNECTION_ERROR: _converter(player_connection_error, models.Message),
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
