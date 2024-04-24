import requests
import allure
from base.base_api import BaseAPI
from config.links import CommentDataLink
from schema.comment import Comment
from builder.payload import CreateCommentDate
from enums.error_message import ErrorMessage


class CreateComment(BaseAPI):
    SCHEMA = Comment

    def __init__(self, authorization):
        super().__init__(authorization)
        self.url = CommentDataLink()
        self.payload = CreateCommentDate()

    def request_create_comment(self, post, commentCount=1):
        with allure.step(f'Create {commentCount} comment(s)'):
            for i in range(commentCount):
                self.response = requests.post(
                    url=self.url.CREATE_COMMENT,
                    headers=self.authorization,
                    json=self.payload.data_comment(post.owner.id, post.id)
                    )
                self.response_json = self.response.json()
                self.check_response_is_200()
                self.check_validate()
                self.attach_response()

    @allure.step('Check user id in comment')
    def check_id_user_in_comment(post, response):
        assert response.owner.id == post.owner.id, ErrorMessage.ERROR_USER_ID_COMMENT

    @allure.step('Check post id in comment')
    def check_id_post_in_comment(post, response):
        assert response.post == post.id, ErrorMessage.ERROR_POST_ID_COMMENT

