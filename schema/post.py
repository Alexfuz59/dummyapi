import datetime as dt
from pydantic import BaseModel, field_validator, HttpUrl, ConfigDict, ValidationInfo, ValidationError
from typing import List, Optional, Union
from schema.user_preview import UserModel


class Post(BaseModel):
    model_config = ConfigDict(str_max_length=200)
    id: str
    text: Optional[str] = None
    image: HttpUrl
    likes: Optional[int] = 0
    link: Optional[Union[HttpUrl, str]] = None
    tags: Optional[List[str]] = None
    publishDate: str
    updatedDate: Optional[str] = None
    owner: UserModel

    @field_validator('text')
    def check_len_text(cls, text):
        if 1000 < len(text) < 6:
            raise ValueError('Invalid text length')
        return text

    @field_validator('publishDate')
    def check_datetime_registration(cls, publishDate):
        current_time = dt.datetime.now()
        registerTime = publishDate.replace('T', ' ').replace('Z', '')
        registerTime = dt.datetime.strptime(registerTime, '%Y-%m-%d %H:%M:%S.%f')
        assert registerTime < current_time, 'Invalid date of post registration '
        return publishDate

    @field_validator('updatedDate')
    def check_update_datetime(cls, updatedDate, info: ValidationInfo):
        registerTime = info.data['publishDate'].replace('T', ' ').replace('Z', '')
        registerTime = dt.datetime.strptime(registerTime, '%Y-%m-%d %H:%M:%S.%f')
        updatedTime = updatedDate.replace('T', ' ').replace('Z', '')
        updatedTime = dt.datetime.strptime(updatedTime, '%Y-%m-%d %H:%M:%S.%f')
        if registerTime > updatedTime :
            raise ValueError('Invalid date of post updated')
        return updatedDate
