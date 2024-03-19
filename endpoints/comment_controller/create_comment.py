import requests
import allure
from base.base_api import BaseAPI
from config.links import CommentDataLink
from schema.comment import Comment
from builder.payload import CreateCommentDate


class CreateComment(BaseAPI):
    SCHEMA = Comment

    def __init__(self):
        super().__init__()
        self.payload = CreateCommentDate()
        self.url = CommentDataLink()

    def request_create_comment(self, headers, post, commentCount=1):
        with allure.step(f'Create {commentCount} comment(s)'):
            for i in range(commentCount):
                self.response = requests.post(
                    url=self.url.CREATE_COMMENT,
                    headers=headers,
                    json=self.payload.data_comment(post.owner.id, post.id)
                    )
                self.response_json = self.response.json()
                self.check_response_is_200()
                self.check_validate()
                self.attach_response()

    @allure.step('Check user id in comment')
    def check_id_user_in_comment(post, response):
        assert response.owner.id == post.owner.id, 'Invalid user ID in comment'

    @allure.step('Check post id in comment')
    def check_id_post_in_comment(post, response):
        assert response.post == post.id, 'Invalid post ID in comment'

