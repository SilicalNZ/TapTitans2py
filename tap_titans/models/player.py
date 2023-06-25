from typing import Optional

from pydantic import Field

from tap_titans.models.code import PlayerCode
from tap_titans.utils.base import BaseModel


class Player(BaseModel):
    name: str | None = Field(default=None)
    player_code: PlayerCode | None = Field(default=None)
