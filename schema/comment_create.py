from pydantic import BaseModel, Field


class CommentCreate(BaseModel):
    message: str = Field(min_length=2, max_length=500)
    owner: str
    post: str
