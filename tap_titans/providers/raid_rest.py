from dataclasses import dataclass

import aiohttp

from tap_titans.abcs import raid_rest as abc
from tap_titans.utils.http_method import Method


_BASE_URL = "https://tt2-public.gamehivegames.com/api/raid"


@dataclass
class RaidRestAPI(abc.RaidRestABC):
    async def _request(
            self,
            *,
            method: Method,
            endpoint: str = "",
            payload: None | dict = None,
            params: None | dict = None,
    ) -> dict:
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.request(
                    method.value,
                    f"{_BASE_URL}{endpoint}",
                    json=payload,
                    params=params,
            ) as resp:
                return await resp.json()

    async def subscribe(self, player_tokens: list[str]) -> abc.SubscribeResp:
        result = await self._request(
            method=Method.POST,
            endpoint="/subscribe",
            payload = {
                "player_tokens": player_tokens,
            },
        )

        return abc.SubscribeResp(**result)

    async def unsubscribe(self, player_tokens: list[str]) -> abc.SubscribeResp:
        result = await self._request(
            method=Method.POST,
            endpoint="/unsubscribe",
            payload={
                "player_tokens": player_tokens,
            },
        )

        return abc.SubscribeResp(**result)
