import requests
import allure
from base.base_api import BaseAPI
from config.links import CommentDataLink
from schema.comment_list import DataListComment


class ListCommentByUser(BaseAPI):
    SCHEMA = DataListComment

    @allure.step('Request comment list by user')
    def request_list_comment_by_user(self, headers, user_id):
        self.response = requests.get(url=f'{CommentDataLink.GET_LIST_COMMENT_BY_USER}/{user_id}/comment', headers=headers)
        self.response_json = self.response.json()

    @allure.step('Check user id in comment list')
    def check_id_user_in_comment_list(self, response, comment):
        assert response.data[0].owner.id == comment.owner.id, 'Invalid user ID in comment list'


