from pydantic import BaseModel, RootModel
from typing import List

class Post(BaseModel):
    user_id: int
    id: int
    title: str
    body: str

class PostList(RootModel[List[Post]]):
    pass
