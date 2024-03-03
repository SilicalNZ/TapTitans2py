from dataclasses import dataclass

import aiohttp

from tap_titans.abcs import rest_api as abc
from tap_titans.abcs.rest_api import UnknownError, SubscribeResp, ClanDataResp, PlayerDataProperties, ClanDataProperties, PlayerData
from tap_titans.utils.http_method import Method


_BASE_URL = "https://tt2-public.gamehivegames.com"


@dataclass
class RestAPI(abc.RestAPIABC):
    auth: str

    async def _request(
            self,
            *,
            method: Method,
            endpoint: str = "",
            payload: None | dict = None,
            params: None | dict = None,
    ) -> str | UnknownError:
        async with aiohttp.ClientSession(raise_for_status=True, headers={"API-Authenticate": self.auth}) as session:
            async with session.request(
                    method.value,
                    f"{_BASE_URL}{endpoint}",
                    json=payload,
                    params=params,
            ) as resp:
                result = await resp.text()

                try:
                    return UnknownError.decode_json(result)
                except:
                    return result

    async def subscribe(self, player_tokens: list[str]) -> SubscribeResp | UnknownError:
        result = await self._request(
            method=Method.POST,
            endpoint="/raid/subscribe",
            payload={
                "player_tokens": player_tokens,
            },
        )

        return SubscribeResp.decode_json(result) if isinstance(result, str) else result

    async def unsubscribe(self, player_tokens: list[str]) -> SubscribeResp | UnknownError:
        result = await self._request(
            method=Method.POST,
            endpoint="/raid/unsubscribe",
            payload={
                "player_tokens": player_tokens,
            },
        )

        return SubscribeResp.decode_json(result) if isinstance(result, str) else result

    async def clan_data(self, player_token: str, properties: tuple[ClanDataProperties, ...]) -> abc.ClanDataResp | UnknownError:
        result = await self._request(
            method=Method.POST,
            endpoint="/raid/clan_data",
            payload={
                "player_token": player_token,
                "properties": [i.value for i in properties],
            },
        )

        return ClanDataResp.decode_json(result) if isinstance(result, str) else result

    async def player_data(self, player_token: str, properties: tuple[PlayerDataProperties, ...]) -> PlayerData | UnknownError:
        result = await self._request(
            method=Method.POST,
            endpoint="/player/data",
            payload={
                "player_token": player_token,
                "properties": [i.value for i in properties],
            },
        )

        return PlayerData.decode_json(result) if isinstance(result, str) else result
