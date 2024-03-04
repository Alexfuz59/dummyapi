from pydantic import BaseModel, Field, HttpUrl
from enums.user_enums import Title
from typing import Optional


class UserModel(BaseModel):
    id: str
    title: Optional[Title] = None
    firstName: str = Field(min_length=2, max_length=52)
    lastName: str = Field(min_length=2, max_length=52)
    picture: HttpUrl
