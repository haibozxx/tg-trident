
import typing
from pydantic import BaseModel


class Response(BaseModel):
    msg: str = ""
    code: int = 0
    data: typing.Any = {}