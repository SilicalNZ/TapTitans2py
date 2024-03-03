from msgspec import Struct as msgspecStruct, json, field, convert

__all__ = (
    "Struct",
)


class Struct(msgspecStruct):
    @classmethod
    def decode_json(cls, data: str | bytes):
        return json.decode(data, type=cls, strict=False)

    def encode_json(self) -> bytes:
        return json.encode(self)

    @classmethod
    def decode_dict(cls, data: dict):
        return convert(data, type=cls, strict=False)
