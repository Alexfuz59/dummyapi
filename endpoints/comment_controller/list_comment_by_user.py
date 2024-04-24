import requests
import allure
from base.base_api import BaseAPI
from config.links import CommentDataLink
from schema.comment_list import DataListComment
from enums.error_message import ErrorMessage


class ListCommentByUser(BaseAPI):
    SCHEMA = DataListComment

    def __init__(self, authorization):
        super().__init__(authorization)
        self.url = CommentDataLink()

    @allure.step('Request comment list by user')
    def request_list_comment_by_user(self, user_id):
        self.response = requests.get(
            url=self.url.GET_LIST_COMMENT_BY_USER(user_id),
            headers=self.authorization
        )
        self.response_json = self.response.json()
        self.attach_response()

    @allure.step('Check user id in comment list')
    def check_id_user_in_comment_list(self, response, comment):
        assert response.data[0].owner.id == comment.owner.id,\
            ErrorMessage.ERROR_USER_ID_COMMENT_LIST


