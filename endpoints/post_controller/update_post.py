import requests
import allure
from base.base_api import BaseAPI
from config.links import PostDataLink
from schema.post import Post
from builder.payload import UpdatePostDate


class UpdatePost(BaseAPI):
    SCHEMA = Post

    def __init__(self, authorization):
        super().__init__(authorization)
        self.url = PostDataLink()
        self.payload = UpdatePostDate()

    @allure.step('Update post')
    def request_update_post(self, post):
        self.response = requests.put(url=self.url.UPDATE_POST(post.id),
                                     headers=self.authorization,
                                     data=self.payload.update_post()
        )
        self.response_json = self.response.json()
        self.attach_response()

    @allure.step('Checking for changes to the post data')
    def check_update_post(self, payload, response):
        assert payload.text != response.text, 'text update error'
        assert payload.image != response.image, 'image update error'
        assert payload.link != response.link, 'link update error'
        assert payload.tags != response.tags, 'tags update error'
