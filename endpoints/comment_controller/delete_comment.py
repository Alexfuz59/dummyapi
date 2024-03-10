import requests
import allure
from base.base_api import BaseAPI
from config.links import CommentDataLink


class DeleteComment(BaseAPI):
    def __init__(self):
        super().__init__()
        self.url = CommentDataLink()

    @allure.step('Delete comment')
    def request_delete_comment(self, headers, comment):
        self.response = requests.delete(
            url=self.url.DELETE_COMMENT(comment.id),
            headers=headers
            )
        self.response_json = self.response.json()
        self.attach_response()
