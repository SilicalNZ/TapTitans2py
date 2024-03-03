from tap_titans.utils.base import Struct, field


class UnknownErrorContext(Struct):
    extra: dict
    http_code: int
    message: str


class UnknownError(Struct):
    error: UnknownErrorContext = field(name="_error")
