import requests
import allure
from base.base_api import BaseAPI
from config.links import UserDataLink
from schema.user_list import DataListUser


class UserList(BaseAPI):
    SCHEMA = DataListUser

    def __init__(self, authorization ):
        super().__init__(authorization)
        self.url = UserDataLink()

    @allure.step('Request user list')
    def request_user_list(self, auth=None):
        if auth == "noauth":
            headers = {}
        else:
            headers = self.authorization
        self.response = requests.get(url=self.url.GET_LIST,
                                     headers=headers
                                     )
        self.response_json = self.response.json()
        self.attach_response()
