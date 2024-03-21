import requests
import allure
from base.base_api import BaseAPI
from config.links import PostDataLink


class DeletePost(BaseAPI):
    def __init__(self, authorization):
        super().__init__(authorization)
        self.url = PostDataLink()

    @allure.step('Delete post')
    def request_delete_post(self, post):
        self.response = requests.delete(
            url=self.url.DELETE_POST(post.id),
            headers=self.authorization
        )
        self.response_json = self.response.json()
        self.attach_response()