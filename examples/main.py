import asyncio

from tap_titans.providers.providers import *


# ----
# TOKEN should not be provided here, this is purely for an example
# At minimum provide through .env
# ----
AUTH_TOKEN = ""
PLAYER_TOKENS = [""]


# This is just an example function that takes anything or nothing.
# Annotations provide what should be accepted for each event
async def test(anything=None):
    print(anything)


# We have to subscribe after we connect
async def connected(anything=None):
    print("Connected")

    r = RaidRestAPI(AUTH_TOKEN)

    resp = await r.subscribe(PLAYER_TOKENS)
    if len(resp.refused) > 0:
        print("Failed to subscribe to clan with reason:", resp.refused[0].reason)
    else:
        print("Subscribed to clan:", resp.ok[0].clan_code)



wsc = WebsocketClient(
    connected=connected,
    disconnected=test,
    error=test,
    connection_error=test,
    clan_removed=test,
    raid_attack=test,
    raid_start=test,
    clan_added_raid_start=test,
    raid_end=test,
    raid_retire=test,
    raid_cycle_reset=test,
    clan_added_cycle=test,
    raid_target_changed=test,
    setting_validate_arguments=False,
)


asyncio.run(wsc.connect(AUTH_TOKEN))
