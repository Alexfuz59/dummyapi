import allure
from base.base_test import BaseTest
from builder.payload import UpdateUserDate as UpUs


@allure.feature('User controller')
class TestUser(BaseTest):

    @allure.title('Request without authorization')
    def test_no_authorization(self):
        self.get_user_list.request_user_list('noauth')
        self.get_user_list.check_response_is_403()

    @allure.title('Get list of users')
    def test_get_user_list(self):
        self.get_user_list.request_user_list()
        self.get_user_list.check_response_is_200()
        self.get_user_list.check_validate()

    @allure.title('Create new user')
    def test_create_user(self):
        self.create_user.request_create_user()
        self.create_user.check_response_is_200()
        self.create_user.check_validate()

    @allure.title('Update user by id')
    def test_update_user(self, user):
        self.update_user.request_update_user(user, payload=UpUs.data_update())
        self.update_user.check_response_is_200()
        user_after = self.update_user.check_validate()
        self.update_user.check_update_user(user, user_after)

    @allure.title('Update user email by id')
    def test_update_email_user(self, user):
        self.update_user.request_update_user(user, payload=UpUs.update_email())
        self.update_user.check_response_is_403()

    @allure.title('Get user full data by user id')
    def test_get_user(self, user):
        self.get_user.request_user(user)
        self.get_user.check_response_is_200()
        self.get_user.check_validate()

    @allure.title('Delete user by id')
    def test_delete_user(self, user):
        self.delete_user.request_delete_user(user)
        self.delete_user.check_response_is_200()
        self.get_user.request_user(user)
        self.get_user.check_response_is_404()
