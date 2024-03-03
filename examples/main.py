import asyncio

from tap_titans.providers import providers
from tap_titans.models import models


# ----
# TOKEN should not be provided here, this is purely for an example
# At minimum provide through .env
# ----
AUTH_TOKEN = ""
PLAYER_TOKENS = [""]


# We have to subscribe after we connect
async def connected():
    print("Raid Namespace Connected")

    r = providers.RestAPI(AUTH_TOKEN)

    resp = await r.subscribe(PLAYER_TOKENS)
    if len(resp.refused) > 0:
        print("Failed to subscribe to clan with reason:", resp.refused[0].reason)
    else:
        print("Subscribed to clan:", resp.ok[0].clan_code)


# Here is an example of every event type with its corresponding object
# Each message has a param called message. This is a python object that can be navigated with dot notation
# View the corresponding object in the models directory
async def disconnected():
    print("Raid Namespace Disconnected")


async def error(message: models.Message):
    print("Raid Namespace Error", message)


async def connection_error(message: models.Message):
    print("Raid Namespace Connection Error", message)


async def clan_removed(message: models.clan_models.ClanRemoved):
    print("Clan Removed", message)


async def raid_attack_start(message: models.raid_models.RaidAttackStart):
    print("Raid Attack Start", message)


async def raid_attack_end(message: models.raid_models.RaidAttackEnd):
    print("Raid Attack End", message)


async def raid_start(message: models.raid_models.RaidStart):
    print("Raid Start", message)


async def clan_added_raid_start(message: models.raid_models.RaidStartClanAdded):
    print("Clan Added Raid Start", message)


async def raid_end(message: models.raid_models.RaidEnd):
    print("Raid End", message)


async def raid_retire(message: models.raid_models.RaidRetire):
    print("Raid Retire", message)


async def raid_cycle_reset(message: models.raid_models.RaidCycleReset):
    print("Raid Cycle Reset", message)


async def clan_added_cycle(message: models.raid_models.RaidCycleResetClanAdded):
    print("Clan Added Cycle", message)
    print("Raid level of clan", message.raid.level)


async def raid_target_changed(message: models.raid_models.RaidTarget):
    print("Raid Target Changed", message)


async def clan_join(message: models.clan_models.ClanJoin):
    print("Player joined Clan", message)


async def clan_leave(message: models.clan_models.ClanLeave):
    print("Player left Clan", message)


async def clan_kick(message:  models.clan_models.ClanKick):
    print("Player kicked from Clan", message)


async def clan_sync(message: models.clan_models.ClanSync):
    print("Clan Information Updated", message)


async def player_morale(message: models.clan_models.PlayerMorale):
    print("Player collected morale", message)


async def player_connected():
    print("Player Namespace Connected")


async def player_disconnected():
    print("Player Namespace Disconnected")


async def player_error(message: models.Message):
    print("Player Namespace Error", message)


async def player_connection_error(message: models.Message):
    print("Playuer Namespace Connection Error", message)


wsc = providers.WebsocketClient(
    connected=connected,
    disconnected=disconnected,
    error=error,
    connection_error=connection_error,
    clan_removed=clan_removed,
    raid_attack_start=raid_attack_start,
    raid_attack_end=raid_attack_end,
    raid_start=raid_start,
    clan_added_raid_start=clan_added_raid_start,
    raid_end=raid_end,
    raid_retire=raid_retire,
    raid_cycle_reset=raid_cycle_reset,
    clan_added_cycle=clan_added_cycle,
    raid_target_changed=raid_target_changed,
    setting_validate_arguments=True,
    clan_join=clan_join,
    clan_leave=clan_leave,
    clan_kick=clan_kick,
    clan_sync=clan_sync,
    player_morale=player_morale,
    player_connected=player_connected,
    player_disconnected=player_disconnected,
    player_error=player_error,
    player_connection_error=player_connection_error,
)


asyncio.run(wsc.connect(AUTH_TOKEN))
