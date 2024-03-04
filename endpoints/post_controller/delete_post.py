import requests
import allure
from base.base_api import BaseAPI
from config.links import PostDataLink


class DeletePost(BaseAPI):
    @allure.step('Delete post')
    def request_delete_post(self, headers, post):
        self.response = requests.delete(url=f'{PostDataLink.DELETE_POST}/{post.id}', headers=headers)
        self.response_json = self.response.json()