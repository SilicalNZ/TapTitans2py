from dataclasses import dataclass

import aiohttp

from tap_titans.abcs import public_api as abc
from tap_titans.abcs.public_api import HolidayEventBreakpoints, MasterTierLeaderboard, GlobalRaidInfo, UnknownError
from tap_titans.utils.http_method import Method


__all__ = (
    "PublicAPI",
    "HolidayEventBreakpoints",
    "MasterTierLeaderboard",
    "GlobalRaidInfo",
    "UnknownError",
)


_BASE_URL = "https://tt2.gamehivegames.com"


@dataclass
class PublicAPI(abc.PublicAPIABC):
    async def _request(
            self,
            *,
            endpoint: str = "",
            payload: None | dict = None,
            params: None | dict = None,
    ) -> str | UnknownError:
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.request(
                    Method.GET,
                    f"{_BASE_URL}{endpoint}",
                    json=payload,
                    params=params,
            ) as resp:
                result = await resp.text()

                try:
                    return UnknownError.decode_json(result)
                except:
                    return result

    async def get_global_raid_info(self) -> GlobalRaidInfo | UnknownError:
        result = await self._request(
            endpoint="/global_raid/info",
        )

        return GlobalRaidInfo.decode_json(result) if isinstance(result, str) else result

    async def get_master_tier_leaderboard(self) -> MasterTierLeaderboard | UnknownError:
        result = await self._request(
            endpoint="/clan/public/master_tier_leaderboard",
        )

        return MasterTierLeaderboard.decode_json(result) if isinstance(result, str) else result

    async def get_holiday_event_breakpoints(self) -> HolidayEventBreakpoints | UnknownError:
        result = await self._request(
            endpoint="/holiday_event/breakpoint",
        )

        return HolidayEventBreakpoints.decode_json(result) if isinstance(result, str) else result
