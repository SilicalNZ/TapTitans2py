import abc
from datetime import datetime

from tap_titans.abcs.error import UnknownError
from tap_titans.utils.base import Struct


__all__ = (
    "GlobalRaidInfo",
    "MasterTierLeaderboardPlacement",
    "MasterTierLeaderboard",
    "HolidayEventBreakpoint",
    "HolidayEventBreakpoints",
    "PublicAPIABC",
    "UnknownError",
)


class GlobalRaidInfo(Struct):
    start_date: datetime
    end_date: datetime
    current_phase: int
    current_hp: int
    total_hp: int


class MasterTierLeaderboardPlacement(Struct):
    rank: int
    name: str
    code: str
    level: int


class MasterTierLeaderboard(Struct):
    season_id: int
    leaderboard: tuple[MasterTierLeaderboardPlacement, ...]


class HolidayEventBreakpoint(Struct):
    percentile: float
    currency: int


class HolidayEventBreakpoints(Struct):
    holiday_event_id: str
    breakpoint: tuple[HolidayEventBreakpoint, ...]


class PublicAPIABC(metaclass=abc.ABCMeta):

    # https://discord.com/channels/352838812646506497/1009101602570895400/1009110991713357824
    @abc.abstractmethod
    async def get_global_raid_info(self) -> GlobalRaidInfo | UnknownError:
        raise NotImplementedError()

    # https://discord.com/channels/352838812646506497/1009101602570895400/1009112684828033167
    @abc.abstractmethod
    async def get_master_tier_leaderboard(self) -> MasterTierLeaderboard | UnknownError:
        raise NotImplementedError()

    # https://discord.com/channels/352838812646506497/1009101602570895400/1065030272585834557
    @abc.abstractmethod
    async def get_holiday_event_breakpoints(self) -> HolidayEventBreakpoints | UnknownError:
        raise NotImplementedError()
