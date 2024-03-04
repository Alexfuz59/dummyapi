import requests
import allure
from base.base_api import BaseAPI
from config.links import UserDataLink
from schema.user_full import User
from model.data_generator import UpdateUserDate


class UpdateUser(BaseAPI):
    SCHEMA = User
    payload_upd = UpdateUserDate.data_update()

    @allure.step('Update user data')
    def request_update_user(self, user_before, headers, model=payload_upd):
        self.response = requests.put(f'{UserDataLink.UPDATE_USER}/{user_before.id}', headers=headers, data=model)
        self.response_json = self.response.json()
        self.payload = self.payload_upd

    @allure.step('Checking changes to user data')
    def check_update_user(self, user_before, user_after):
        assert user_before.firstName != user_after.firstName, 'firstName has not been updated'
        assert user_before.lastName != user_after.lastName, 'lastName has not been updated'
