Tap Titans 2 (Python wrapper)
========
A drop in library to provide requests and responses to the various Tap Titans 2 APIs

## Overview

- Modern Pythonic API using `async`/`await` syntax
- Easy to use with an object-oriented design
- Cross version compatibility. 
- Interfaces for all TapTitans2 APIs; SocketIO, Rest, PublicAPI
- Fully annotated using python typehinting

## Getting Started

- You need to request a Player Token of a clan Master or GrandMaster. They can create one for you by going to the `Settings -> Player API Tokens` in the app
- You will need to join the [GameHive Discord](https://discord.com/invite/gamehive) and ask for an API Token in the channel #app-token-request.
- You need to be prepared to run this 24/7 with a stable connection. GameHive does not store events and so if this isn't running, events will be skipped with no way to get them again. I recommend [Google Compute Engine](https://cloud.google.com/free/docs/free-cloud-features#compute) which has a permanent free tier on a E2-micro instance.

## Installing
**Python 3.10 or higher is required**
[Download Here](https://www.python.org/downloads/)

Installation is done by using the [pip install](https://pip.pypa.io/en/stable/installation/) command. Usually it is already included with the python install.

To install the library
```
# Linux/macOS
python3 -m pip install -U git+https://github.com/SilicalNZ/TapTitans2py

# Windows
py -3 -m pip install -U git+https://github.com/SilicalNZ/TapTitans2py
```

## Quick Example

```py
import asyncio
from tap_titans.providers import providers
from tap_titans.models import models

AUTH_TOKEN = "auth_token"
PLAYER_TOKENS = ["player_token"]

async def connected():
    print("Connected")

    r = providers.RestAPI(AUTH_TOKEN)

    resp = await r.subscribe(PLAYER_TOKENS)
    if len(resp.refused) > 0:
        print("Failed to subscribe to clan with reason:", resp.refused[0].reason)
    else:
        print("Subscribed to clan:", resp.ok[0].clan_code)

async def clan_added_cycle(message: models.raid_models.RaidCycleResetClanAdded):
    print("Clan Added Cycle", message)
    print("Raid level of clan", message.raid.level)

async def raid_attack_end(message: models.raid_models.RaidAttackEnd):
    print("Raid Attack", message)

async def player_connected():
    print("Player WS is connected, can now use the rest API /player endpoints")
    r = providers.RestAPI(AUTH_TOKEN)

    resp = await r.player_data(PLAYER_TOKENS[0], providers.PlayerDataProperties.all())

    print("Name of the player who owns the token:", resp.name)

websocket = providers.WebsocketClient(
    connected=connected,
    raid_attack_end=raid_attack_end,
    clan_added_cycle=clan_added_cycle,
    setting_validate_arguments=True,
    player_connected=player_connected,
)

asyncio.run(websocket.connect(AUTH_TOKEN))
```
Find more examples in the [examples directory](https://github.com/SilicalNZ/TapTitans2py/blob/master/examples/main.py)

## Getting Help

- Report bugs in the [issue tracker](https://github.com/SilicalNZ/TapTitans2py/issues)
- Reach out on Discord to the maintainer `silical`
- Join the [Discord Server](https://discord.gg/FyYR62hHHB)


## Links

- [TapTitans2 API Documentation](https://tt2-docs.gamehivegames.com/)
- [GameHive Discord](https://discord.com/invite/gamehive)
- [SocketIO Specification Documentation](https://socket.io/docs/v4/)
