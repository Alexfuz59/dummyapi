import requests
import allure
from base.base_api import BaseAPI
from config.links import CommentDataLink


class DeleteComment(BaseAPI):
    def __init__(self, authorization):
        super().__init__(authorization)
        self.url = CommentDataLink()

    @allure.step('Delete comment')
    def request_delete_comment(self, comment):
        self.response = requests.delete(
            url=self.url.DELETE_COMMENT(comment.id),
            headers=self.authorization
            )
        self.response_json = self.response.json()
        self.attach_response()
