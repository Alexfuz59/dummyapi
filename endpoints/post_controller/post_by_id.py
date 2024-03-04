import requests
import allure
from base.base_api import BaseAPI
from config.links import PostDataLink
from schema.post import Post

class PostByID(BaseAPI):
    SCHEMA = Post

    @allure.step('Get post by id user')
    def request_post_by_id(self, headers, post):
        self.response = requests.get(url=f'{PostDataLink.GET_POST_BY_ID}/{post.id}', headers=headers)
        self.response_json = self.response.json()

    @allure.step('Checking the requested post by id')
    def check_post_by_id(self, post, response):
        assert post == response, 'Invalid search by post id'
