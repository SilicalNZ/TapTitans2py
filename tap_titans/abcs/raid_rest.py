import abc
from dataclasses import dataclass

from tap_titans.models.code import ClanCode
from tap_titans.utils.base import BaseModel



__all__ = (
    "RaidRestABC",
    "SubscribeResp",
    "SubscribeRespOK",
    "SubscribeRespRefused",
)


class SubscribeRespOK(BaseModel):
    token: str
    clan_code: ClanCode


class SubscribeRespRefused(BaseModel):
    token: str
    reason: str


class SubscribeResp(BaseModel):
    ok: tuple[SubscribeRespOK, ...]
    refused: tuple[SubscribeRespRefused, ...]


@dataclass
class RaidRestABC(metaclass=abc.ABCMeta):
    # https://tt2-docs.gamehivegames.com/rest/

    @abc.abstractmethod
    async def subscribe(self, player_tokens: list[str]) -> SubscribeResp:
        raise NotImplementedError()

    @abc.abstractmethod
    async def unsubscribe(self, player_tokens: list[str]) -> SubscribeResp:
        raise NotImplementedError()
