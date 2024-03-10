import requests
import allure
from base.base_api import BaseAPI
from config.links import PostDataLink
from schema.post import Post
from model.payload import RegisterPost


class CreatePost(BaseAPI):
    SCHEMA = Post

    def __init__(self):
        super().__init__()
        self.url = PostDataLink()
        self.payload = RegisterPost()

    def request_create_post(self, headers, owner, postCount=1):
        with allure.step(f'Create {postCount} post(s)'):
            for i in range(postCount):
                self.response = requests.post(
                    url=self.url.CREATE_POST,
                    headers=headers,
                    json=self.payload.post_data(owner.id)
                )
                self.response_json = self.response.json()
                self.check_response_is_200()
                self.check_validate()
                self.attach_response()



