import requests
import allure
from base.base_api import BaseAPI
from config.links import UserDataLink
from schema.user_list import DataListUser


class UserList(BaseAPI):
    SCHEMA = DataListUser

    @allure.step('Request user list')
    def request_user_list(self, headers={}):
        self.response = requests.get(url=UserDataLink.GET_LIST, headers=headers)
        self.response_json = self.response.json()
