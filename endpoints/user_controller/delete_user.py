import requests
import allure
from base.base_api import BaseAPI
from config.links import UserDataLink


class DeleteUser(BaseAPI):
    def __init__(self, authorization):
        super().__init__(authorization)
        self.url = UserDataLink()

    @allure.step('Delete user')
    def request_delete_user(self, user):
        self.response = requests.delete(url=self.url.DELETE_USER(user.id),
                                        headers=self.authorization
                                        )
        self.response_json = self.response.json()
        self.attach_response()
