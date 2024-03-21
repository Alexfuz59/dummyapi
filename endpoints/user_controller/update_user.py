import requests
import allure
from base.base_api import BaseAPI
from config.links import UserDataLink
from schema.user_full import User
from builder.payload import UpdateUserDate


class UpdateUser(BaseAPI):
    SCHEMA = User

    def __init__(self, authorization):
        super().__init__(authorization)
        self.url = UserDataLink()

    @allure.step('Update user data')
    def request_update_user(self, user, payload):
        self.response = requests.put(url=self.url.UPDATE_USER(user.id),
                                     headers=self.authorization,
                                     json=payload
                                     )
        self.response_json = self.response.json()
        self.payload = payload
        self.attach_response()

    @allure.step('Checking changes to user data')
    def check_update_user(self, user_before, user_after):
        assert user_before.firstName != user_after.firstName, 'firstName has not been updated'
        assert user_before.lastName != user_after.lastName, 'lastName has not been updated'
