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
    print("Connected")

    r = providers.RaidRestAPI(AUTH_TOKEN)

    resp = await r.subscribe(PLAYER_TOKENS)
    if len(resp.refused) > 0:
        print("Failed to subscribe to clan with reason:", resp.refused[0].reason)
    else:
        print("Subscribed to clan:", resp.ok[0].clan_code)


# Here is an example of every event type with its corresponding object
# Each message has a param called message. This is a python object that can be navigated through dot notation
# View the corresponding object in the models directory
async def disconnected():
    print("Disconnected")


async def error(message: models.Message):
    print("Error", message)


async def connection_error(message: models.Message):
    print("Connection Error", message)


async def clan_removed(message: models.ClanRemoved):
    print("Clan Removed", message)


async def raid_attack(message: models.RaidAttack):
    print("Raid Attack", message)


async def raid_start(message: models.RaidStart):
    print("Raid Start", message)


async def clan_added_raid_start(message: models.RaidStart):
    print("Clan Added Raid Start", message)


async def raid_end(message: models.RaidEnd):
    print("Raid End", message)


async def raid_retire(message: models.RaidRetire):
    print("Raid Retire", message)


async def raid_cycle_reset(message: models.RaidCycleReset):
    print("Raid Cycle Reset", message)


async def clan_added_cycle(message: models.RaidCycleReset):
    print("Clan Added Cycle", message)
    print("Raid level of clan", message.raid.level)


async def raid_target_changed(message: models.RaidTarget):
    print("Raid Target Changed", message)


wsc = providers.WebsocketClient(
    connected=connected,
    disconnected=disconnected,
    error=error,
    connection_error=connection_error,
    clan_removed=clan_removed,
    raid_attack=raid_attack,
    raid_start=raid_start,
    clan_added_raid_start=clan_added_raid_start,
    raid_end=raid_end,
    raid_retire=raid_retire,
    raid_cycle_reset=raid_cycle_reset,
    clan_added_cycle=clan_added_cycle,
    raid_target_changed=raid_target_changed,
    setting_validate_arguments=True,
)


asyncio.run(wsc.connect(AUTH_TOKEN))
