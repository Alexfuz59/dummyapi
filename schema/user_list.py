from pydantic import BaseModel, field_validator
from pydantic.types import List
from schema.user_preview import UserModel


class DataListUser(BaseModel):
    data: List[UserModel]
    total: int
    page: int
    limit: int

    @field_validator('limit')
    def check_limit(cls, limit):
        if limit != 20:
            raise ValueError('Invalid value in the limit field')
        return limit

    @field_validator('data')
    def check_len_data(cls, data):
        if len(data) != 20:
            raise ValueError('Incorrect number of users in the user list')
        return data


