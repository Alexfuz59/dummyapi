import allure
import pytest
from base.base_test import BaseTest


@allure.feature('Comment controller')
class TestComment(BaseTest):

    @pytest.fixture()
    def comment(self, authorization, post):
        self.create_comment.request_create_comment(authorization, post)
        comment = self.create_comment.check_validate()
        return comment

    @allure.title('Get list of comments')
    def test_comment_get_list(self, authorization):
        self.comment_get_list.request_comment_list(authorization)
        self.comment_get_list.check_response_is_200()
        self.comment_get_list.check_validate()

    @allure.title('Create new comment')
    @pytest.mark.parametrize('commentCount', [1, 2, 10])
    def test_create_comment(self, authorization, post, commentCount):
        self.create_comment.request_create_comment(authorization, post, commentCount)
        self.list_comment_by_post.request_list_comment_by_post(authorization, post.id)
        self.list_comment_by_post.check_response_is_200()
        responsePost = self.list_comment_by_post.check_validate()
        self.list_comment_by_post.check_total_object(commentCount, responsePost.total)
        self.list_comment_by_user.request_list_comment_by_user(authorization, post.owner.id)
        self.list_comment_by_user.check_response_is_200()
        responseUser = self.list_comment_by_user.check_validate()
        self.list_comment_by_user.check_total_object(commentCount, responseUser.total)

    @allure.title('Delete comment by id')
    def test_delete_comment(self, authorization, comment):
        self.delete_comment.request_delete_comment(authorization, comment)
        self.delete_comment.check_response_is_200()

    @allure.title('Get list of comments for specific user')
    def test_list_comment_by_user(self, authorization, comment):
        self.list_comment_by_user.request_list_comment_by_user(authorization, comment.owner.id)
        self.list_comment_by_user.check_response_is_200()
        response = self.list_comment_by_user.check_validate()
        self.list_comment_by_user.check_id_user_in_comment_list(response, comment)
        self.list_comment_by_user.check_total_object(response.total)

    @allure.title('Get list of comments for specific post')
    def test_list_comment_by_post(self, authorization, comment):
        self.list_comment_by_post.request_list_comment_by_post(authorization, comment.post)
        self.list_comment_by_post.check_response_is_200()
        response = self.list_comment_by_post.check_validate()
        self.list_comment_by_post.check_total_object(response.total)
        self.list_comment_by_post.check_id_post_in_comment_list(response, comment)