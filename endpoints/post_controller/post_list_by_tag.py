import requests
import allure
from base.base_api import BaseAPI
from config.links import PostDataLink
from schema.post_list import DataListPost


class PostListByTag(BaseAPI):
    SCHEMA = DataListPost

    def __init__(self):
        super().__init__()
        self.url = PostDataLink()

    @allure.step('User tag list request')
    def request_post_list_by_tag(self, headers, user):
        self.response = requests.get(
            url=self.url.GET_LIST_BY_TAG(user.owner.id),
            headers=headers
        )
        self.response_json = self.response.json()
        self.attach_response()