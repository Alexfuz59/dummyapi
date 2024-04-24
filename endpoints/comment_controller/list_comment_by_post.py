import requests
import allure
from base.base_api import BaseAPI
from config.links import CommentDataLink
from schema.comment_list import DataListComment
from enums.error_message import ErrorMessage


class ListCommentByPost(BaseAPI):
    SCHEMA = DataListComment

    def __init__(self, authorization):
        super().__init__(authorization)
        self.url = CommentDataLink()

    @allure.step('Request comment list by post')
    def request_list_comment_by_post(self, post_id):
        self.response = requests.get(
            url=self.url.GET_LIST_COMMENT_BY_POST(post_id),
            headers=self.authorization
        )
        self.response_json = self.response.json()
        self.attach_response()

    @allure.step('Check post id in comment list')
    def check_id_post_in_comment_list(self, response, comment):
        assert response.data[0].post == comment.post,\
            ErrorMessage.ERROR_POST_ID_COMMENT_LIST
