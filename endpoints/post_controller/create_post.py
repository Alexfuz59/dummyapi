import requests
import allure
from base.base_api import BaseAPI
from config.links import PostDataLink
from schema.post import Post
from model.data_generator import RegisterPost


class CreatePost(BaseAPI):
    SCHEMA = Post

    def __init__(self):
        self.payload_post = RegisterPost.post_data()

    def request_create_post(self, headers, owner, postCount=1):
        with allure.step(f'Create {postCount} post(s)'):
            for i in range(postCount):
                body = self.payload_post
                body['owner'] = owner.id
                self.response = requests.post(url=PostDataLink.CREATE_POST, headers=headers, data=body)
                self.response_json = self.response.json()
                self.check_response_is_200()
                self.check_validate()



