import requests
import allure
from base.base_api import BaseAPI
from config.links import CommentDataLink
from schema.comment_list import DataListComment


class CommentList(BaseAPI):
    SCHEMA = DataListComment

    def __init__(self, authorization):
        super().__init__(authorization)
        self.url = CommentDataLink()

    @allure.step('Request comment list')
    def request_comment_list(self):
        self.response = requests.get(
            url=self.url.GET_LIST_COMMENT,
            headers=self.authorization
        )
        self.response_json = self.response.json()
        self.attach_response()

