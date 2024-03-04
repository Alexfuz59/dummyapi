import datetime as dt
from pydantic import BaseModel, Field, field_validator
from schema.post_preview import UserModel


class Comment(BaseModel):
    id: str
    message: str = Field(min_length=2, max_length=500)
    post: str
    publishDate: str
    owner: UserModel

    @field_validator('publishDate')
    def check_datetime_registration(cls, publishDate):
        current_time = dt.datetime.now()
        registerTime = publishDate.replace('T', ' ').replace('Z', '')
        registerTime = dt.datetime.strptime(registerTime, '%Y-%m-%d %H:%M:%S.%f')
        assert registerTime < current_time, 'Invalid date of comment creation'
        return publishDate

