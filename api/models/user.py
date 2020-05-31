from typing import List

from pydantic import BaseModel

from api.enums import Gender


class User(BaseModel):
    name: str
    gender: Gender
    genres: List[str]
    casts: List[str]
