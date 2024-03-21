import allure
import json
from allure_commons.types import AttachmentType


class BaseAPI:
    response = None
    response_json = None
    payload = None
    SCHEMA = None

    def __init__(self, authorization):
        self.authorization = authorization

    @allure.step('Check validate schema')
    def check_validate(self):
        parsed_object = self.SCHEMA.model_validate(self.response_json)
        return parsed_object

    @allure.step('Check response is 200')
    def check_response_is_200(self):
        assert self.response.status_code == 200, f'Error status code {self.response.status_code}'

    @allure.step('Check response is 404')
    def check_response_is_404(self):
        assert self.response.status_code == 404, f'Error status code {self.response.status_code}'

    @allure.step('Check total number of objects in the list')
    def check_total_object(self, objectCount, total_object=1):
        assert total_object == objectCount, 'Wrong total number of objects'

    @allure.step('Check response is 404')
    def check_response_is_403(self):
        assert self.response.status_code == 403, f'Error status code {self.response.status_code}'

    @allure.step('Add json to allure report')
    def attach_response(self):
        response = json.dumps(self.response_json, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)
