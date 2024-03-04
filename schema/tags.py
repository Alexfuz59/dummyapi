from pydantic import BaseModel
from typing import List


class DataListTags(BaseModel):
    data: List[str]
