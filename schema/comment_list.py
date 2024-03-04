from pydantic import BaseModel, field_validator
from schema.comment import Comment
from typing import List


class DataListComment(BaseModel):
    data: List[Comment] = None
    total: int
    page: int
    limit: int

    @field_validator('limit')
    def check_limit(cls, limit):
        if limit != 20:
            raise ValueError('Invalid value in the limit field')
        return limit
