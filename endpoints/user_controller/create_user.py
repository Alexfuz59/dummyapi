import requests
import allure
from base.base_api import BaseAPI
from config.links import UserDataLink
from schema.user_full import User
from builder.payload import RegisterUser


class CreateUser(BaseAPI):
    SCHEMA = User

    def __init__(self):
        super().__init__()
        self.url = UserDataLink()
        self.payload = RegisterUser()

    @allure.step('Create user')
    def request_create_user(self, headers):
        self.response = requests.post(url=self.url.CREATE_USER,
                                      headers=headers,
                                      json=self.payload.user_data()
                                      )
        self.response_json = self.response.json()
        self.attach_response()
