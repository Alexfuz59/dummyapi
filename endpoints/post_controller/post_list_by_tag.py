import requests
import allure
from base.base_api import BaseAPI
from config.links import PostDataLink
from schema.post_list import DataListPost


class PostListByTag(BaseAPI):
    SCHEMA = DataListPost

    @allure.step('User tag list request')
    def request_post_list_by_tag(self, headers, user):
        self.response = requests.get(url=f'{PostDataLink.GET_LIST_BY_TAG}/{user.owner.id}/post', headers=headers)
        self.response_json = self.response.json()