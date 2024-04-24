import requests
import allure
from base.base_api import BaseAPI
from config.links import PostDataLink
from schema.post import Post
from enums.error_message import ErrorMessage


class PostByID(BaseAPI):
    SCHEMA = Post

    def __init__(self, authorization):
        super().__init__(authorization)
        self.url = PostDataLink()

    @allure.step('Get post by id user')
    def request_post_by_id(self, post):
        self.response = requests.get(
            url=self.url.GET_POST_BY_ID(post.id),
            headers=self.authorization
        )
        self.response_json = self.response.json()
        self.attach_response()

    @allure.step('Checking the requested post by id')
    def check_post_by_id(self, post, response):
        assert post == response, ErrorMessage.ERROR_POST_ID_SEARCH
