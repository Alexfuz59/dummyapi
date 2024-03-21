import requests
import allure
from base.base_api import BaseAPI
from config.links import TagsDataLink
from schema.tags import DataListTags


class TagsList(BaseAPI):
    SCHEMA = DataListTags

    def __init__(self, authorization):
        super().__init__(authorization)
        self.url = TagsDataLink()

    @allure.step('Get tag list')
    def request_tags_list(self):
        self.response = requests.get(url=self.url.GET_LIST_TAGS,
                                     headers=self.authorization
                                     )
        self.response_json = self.response.json()
        self.attach_response()
