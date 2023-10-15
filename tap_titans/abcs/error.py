from tap_titans.utils.base import BaseModel

from pydantic import Field


class UnknownErrorContext(BaseModel):
    extra: dict
    http_code: int
    message: str


class UnknownError(BaseModel):
    error: UnknownErrorContext = Field(alias="_error")
