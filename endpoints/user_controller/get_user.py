import requests
import allure
from base.base_api import BaseAPI
from config.links import UserDataLink
from schema.user_full import User


class UserGet(BaseAPI):
    SCHEMA = User

    @allure.step('Request user data')
    def request_user(self, user, headers):
        self.response = requests.get(f'{UserDataLink.GET_USER_BY_ID}/{user.id}', headers=headers)
        self.response_json = self.response.json()