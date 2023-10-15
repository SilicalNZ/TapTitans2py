from dataclasses import dataclass

import aiohttp

from tap_titans.abcs import raid_rest as abc
from tap_titans.utils.http_method import Method


_BASE_URL = "https://tt2-public.gamehivegames.com/raid"


@dataclass
class RaidRestAPI(abc.RaidRestABC):
    auth: str

    async def _request(
            self,
            *,
            method: Method,
            endpoint: str = "",
            payload: None | dict = None,
            params: None | dict = None,
    ) -> dict:
        async with aiohttp.ClientSession(raise_for_status=True, headers={"API-Authenticate": self.auth}) as session:
            async with session.request(
                    method.value,
                    f"{_BASE_URL}{endpoint}",
                    json=payload,
                    params=params,
            ) as resp:
                result = await resp.json()

                if result.get("_error") is not None:
                    return abc.UnknownError(**result)

                return result

    async def subscribe(self, player_tokens: list[str]) -> abc.SubscribeResp | abc.UnknownError:
        result = await self._request(
            method=Method.POST,
            endpoint="/subscribe",
            payload={
                "player_tokens": player_tokens,
            },
        )

        return abc.SubscribeResp(**result) if isinstance(result, dict) else result

    async def unsubscribe(self, player_tokens: list[str]) -> abc.SubscribeResp | abc.UnknownError:
        result = await self._request(
            method=Method.POST,
            endpoint="/unsubscribe",
            payload={
                "player_tokens": player_tokens,
            },
        )

        return abc.SubscribeResp(**result) if isinstance(result, dict) else result
