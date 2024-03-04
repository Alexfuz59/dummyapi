import os
import pytest
from dotenv import load_dotenv
from endpoints.user_controller.create_user import CreateUser
from endpoints.user_controller.delete_user import DeleteUser
from endpoints.post_controller.create_post import CreatePost
from endpoints.post_controller.delete_post import DeletePost

load_dotenv()


@pytest.fixture(autouse=True)
def authorization():
    headers = {'app-id': os.getenv('TOKEN')}
    return headers


@pytest.fixture()
def user(authorization):
    create_user = CreateUser()
    delete_user = DeleteUser()
    create_user.request_create_user(authorization)
    create_user.check_response_is_200()
    user = create_user.check_validate()
    yield user
    delete_user.request_delete_user(user, authorization)


@pytest.fixture()
def post(authorization, user):
    create_post = CreatePost()
    delete_post = DeletePost()
    create_post.request_create_post(authorization, user)
    create_post.check_response_is_200()
    post = create_post.check_validate()
    yield post
    delete_post.request_delete_post(authorization, post)
