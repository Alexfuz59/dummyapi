import requests
import allure
from base.base_api import BaseAPI
from config.links import PostDataLink
from schema.post_list import DataListPost


class PostList(BaseAPI):
    SCHEMA = DataListPost

    def __init__(self):
        super().__init__()
        self.url = PostDataLink()

    @allure.step('Request post list')
    def request_post_list(self, headers):
        self.response = requests.get(
            url=self.url.GET_LIST_POST,
            headers=headers
        )
        self.response_json = self.response.json()
        self.attach_response()