import requests
import allure
from base.base_api import BaseAPI
from config.links import PostDataLink
from schema.post import Post
from model.data_generator import UpdatePostDate


class UpdatePost(BaseAPI):
    SCHEMA = Post

    def __init__(self):
        self.payload_post = UpdatePostDate.update_post()

    @allure.step('Update post')
    def request_update_post(self, headers, post):
        self.response = requests.put(url=f'{PostDataLink.UPDATE_POST}/{post.id}', headers=headers, data=self.payload_post)
        self.response_json = self.response.json()

    @allure.step('Checking for changes to the post data')
    def check_update_post(self, payload, response):
        assert payload.text != response.text, 'text update error'
        assert payload.image != response.image, 'image update error'
        assert payload.link != response.link, 'link update error'
        assert payload.tags != response.tags, 'tags update error'
