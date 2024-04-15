import os
import pytest
from dotenv import load_dotenv
from endpoints.user_controller.create_user import CreateUser
from endpoints.user_controller.delete_user import DeleteUser
from endpoints.post_controller.create_post import CreatePost
from endpoints.post_controller.delete_post import DeletePost
from config.environment_allure import EnvironmentAllure

load_dotenv()


@pytest.fixture(autouse=True, scope='function')
def authorization(request):
    authorization = {'app-id': os.getenv('TOKEN')}
    request.cls.authorization = authorization
    return authorization


@pytest.fixture()
def user(authorization):
    create_user = CreateUser(authorization)
    delete_user = DeleteUser(authorization)
    create_user.request_create_user()
    create_user.check_response_is_200()
    user = create_user.check_validate()
    yield user
    delete_user.request_delete_user(user)


@pytest.fixture()
def post(authorization, user):
    create_post = CreatePost(authorization)
    delete_post = DeletePost(authorization)
    create_post.request_create_post(user)
    create_post.check_response_is_200()
    post = create_post.check_validate()
    yield post
    delete_post.request_delete_post(post)


@pytest.fixture(autouse=True, scope='session')
def environment_allure():
    EnvironmentAllure.create_environment()
