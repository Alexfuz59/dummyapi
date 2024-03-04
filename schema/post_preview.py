import datetime as dt
from pydantic import BaseModel, Field, HttpUrl, field_validator
from pydantic.types import List
from pydantic.types import PastDate
from schema.user_preview import UserModel


class PostPreview(BaseModel):
    id: str
    text: str = Field(min_length=6, max_length=52)
    image: HttpUrl
    likes: int
    tags: List[str]
    publishDate: PastDate
    owner: UserModel

    @field_validator('publishDate')
    def check_datetime_registration(cls, publishDate):
        current_time = dt.datetime.now()
        registerTime = publishDate.replace('T', ' ').replace('Z', '')
        registerTime = dt.datetime.strptime(registerTime, '%Y-%m-%d %H:%M:%S.%f')
        assert registerTime < current_time, 'Invalid date of post creation'
        return publishDate