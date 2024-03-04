import requests
import allure
from base.base_api import BaseAPI
from config.links import UserDataLink
from schema.user_full import User
from model.data_generator import RegisterUser


class CreateUser(BaseAPI):
    SCHEMA = User

    def __init__(self):
        self.payload_reg = RegisterUser.user_data()

    @allure.step('Create user')
    def request_create_user(self, headers):
        self.response = requests.post(url=UserDataLink.CREATE_USER, headers=headers, data=self.payload_reg)
        self.response_json = self.response.json()
