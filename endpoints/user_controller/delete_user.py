import requests
import allure
from base.base_api import BaseAPI
from config.links import UserDataLink


class DeleteUser(BaseAPI):
    def __init__(self):
        super().__init__()
        self.url = UserDataLink()

    @allure.step('Delete user')
    def request_delete_user(self, user, headers):
        self.response = requests.delete(url=self.url.DELETE_USER(user.id),
                                        headers=headers
                                        )
        self.response_json = self.response.json()
        self.attach_response()
