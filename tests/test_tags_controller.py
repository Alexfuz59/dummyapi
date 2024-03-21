import allure
from base.base_test import BaseTest


@allure.feature('Tag controller')
class TestTags(BaseTest):

    @allure.title('Get list of tags')
    def test_list_tags(self):
        self.list_tags.request_tags_list()
        self.list_tags.check_response_is_200()
        self.list_tags.check_validate()

