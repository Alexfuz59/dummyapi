from pydantic import BaseModel, field_validator
from typing import List
from schema.post import Post


class DataListPost(BaseModel):
    data: List[Post] = None
    total: int
    page: int
    limit: int

    @field_validator('limit')
    def check_limit(cls, limit):
        if limit != 20:
            raise ValueError('Invalid value in the limit field')
        return limit

