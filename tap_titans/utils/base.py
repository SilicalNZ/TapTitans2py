from __future__ import annotations

from typing import Any
import json

from pydantic import BaseModel as PyDanticBaseModel


__all__ = (
    "BaseModel",
)


class BaseModel(PyDanticBaseModel):
    _omit: set[str] = {}

    @property
    def _omitted_fields(self) -> set[str]:
        return {
            name
            for name in self._omit
            if not getattr(self, name, None)
        }

    def dict(
        self,
        **kwargs,
    ) -> dict[str, Any]:
        return super().dict(exclude=self._omitted_fields)

    def json(
        self,
        **kwargs,
    ) -> str:
        return super().json(exclude=self._omitted_fields)

    def dict_as_valid_json(
        self,
        **kwargs,
    ) -> dict[str, Any]:
        # This is so jank, but it seems Enums do not convert to json unless passed through pydantics json encoder
        # Pydantics json encoder also seems to be a lambda x: x, so I really don't know what is going on
        # Python is just dumb
        return json.loads(self.json(**kwargs))
