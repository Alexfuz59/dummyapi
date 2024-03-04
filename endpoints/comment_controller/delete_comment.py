import requests
import allure
from base.base_api import BaseAPI
from config.links import CommentDataLink


class DeleteComment(BaseAPI):

    @allure.step('Delete comment')
    def request_delete_comment(self, headers, comment):
        self.response = requests.delete(url=f'{CommentDataLink.DELETE_COMMENT}/{comment.id}', headers=headers)
        self.response_json = self.response.json()