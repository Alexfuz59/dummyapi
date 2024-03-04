import requests
import allure
from base.base_api import BaseAPI
from config.links import PostDataLink
from schema.post_list import DataListPost


class PostListByIDUser(BaseAPI):
    SCHEMA = DataListPost

    @allure.step('User post list by id')
    def request_post_list_by_id(self, headers, user_id):
        self.response = requests.get(url=f'{PostDataLink.GET_LIST_BY_USER}/{user_id}/post', headers=headers)
        self.response_json = self.response.json()