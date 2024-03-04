import requests
import allure
from base.base_api import BaseAPI
from config.links import UserDataLink


class DeleteUser(BaseAPI):
    @allure.step('Delete user')
    def request_delete_user(self, user, headers):
        self.response = requests.delete(f'{UserDataLink.DELETE_USER}/{user.id}', headers=headers)
        self.response_json = self.response.json()
