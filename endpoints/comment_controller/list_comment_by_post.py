import requests
import allure
from base.base_api import BaseAPI
from config.links import CommentDataLink
from schema.comment_list import DataListComment


class ListCommentByPost(BaseAPI):
    SCHEMA = DataListComment

    @allure.step('Request comment list by post')
    def request_list_comment_by_post(self, headers, post_id):
        self.response = requests.get(url=f'{CommentDataLink.GET_LIST_COMMENT_BY_POST}/{post_id}/comment',
                                     headers=headers)
        self.response_json = self.response.json()

    @allure.step('Check post id in comment list')
    def check_id_post_in_comment_list(self, response, comment):
        assert response.data[0].post == comment.post, 'Invalid post ID in comment list'