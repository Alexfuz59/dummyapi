import allure
import pytest
from base.base_test import BaseTest


@allure.feature('Post controller')
class TestPost(BaseTest):

    @pytest.fixture()
    def post(self, authorization, user):
        self.create_post.request_create_post(authorization, user)
        self.create_post.check_response_is_200()
        post = self.create_post.check_validate()
        yield post
        self.delete_post.request_delete_post(authorization, post)

    @allure.title('Get list of posts')
    def test_get_post_list(self, authorization):
        self.post_list.request_post_list(authorization)
        self.post_list.check_response_is_200()
        self.post_list.check_validate()

    @allure.title('Create new post')
    @pytest.mark.parametrize('postCount', [1, 2, 10])
    def test_create_post(self, authorization, user, postCount):
        self.create_post.request_create_post(authorization, user, postCount)
        self.create_post.check_response_is_200()
        self.post_list_by_id_user.request_post_list_by_id(authorization, user.id)
        self.post_list_by_id_user.check_response_is_200()
        response = self.post_list_by_id_user.check_validate()
        self.post_list_by_id_user.check_total_object(postCount, response.total)

    @allure.title('Update post by id')
    def test_update_post(self, authorization, post):
        self.update_post.request_update_post(authorization, post)
        self.update_post.check_response_is_200()
        response = self.update_post.check_validate()
        self.update_post.check_update_post(post, response)

    @allure.title('Delete post by id')
    def test_delete_post(self, authorization, post):
        self.delete_post.request_delete_post(authorization, post)
        self.delete_post.check_response_is_200()
        self.post_by_id.request_post_by_id(authorization, post)
        self.post_by_id.check_response_is_404()

    @allure.title('Get post full data by post id')
    def test_post_by_id(self, authorization, post):
        self.post_by_id.request_post_by_id(authorization, post)
        self.post_by_id.check_response_is_200()
        response = self.post_by_id.check_validate()
        self.post_by_id.check_post_by_id(post, response)

    @allure.title('Get list of posts for specific user')
    def test_post_list_by_id_user(self, authorization, post):
        self.post_list_by_id_user.request_post_list_by_id(authorization, post.owner.id)
        self.post_list_by_id_user.check_response_is_200()
        self.post_list_by_id_user.check_validate()

    @allure.title('Get list of posts for specific tag')
    def test_post_list_by_tag(self, authorization, post):
        self.post_list_by_tag.request_post_list_by_tag(authorization, post)
        self.post_list_by_tag.check_response_is_200()
        self.post_list_by_tag.check_validate()





