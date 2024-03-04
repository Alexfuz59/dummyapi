import pytest
from endpoints.user_controller.get_user_list import UserList
from endpoints.user_controller.create_user import CreateUser
from endpoints.user_controller.update_user import UpdateUser
from endpoints.user_controller.get_user import UserGet
from endpoints.user_controller.delete_user import DeleteUser
from endpoints.post_controller.post_list import PostList
from endpoints.post_controller.create_post import CreatePost
from endpoints.post_controller.update_post import UpdatePost
from endpoints.post_controller.delete_post import DeletePost
from endpoints.post_controller.post_by_id import PostByID
from endpoints.post_controller.post_list_by_id_user import PostListByIDUser
from endpoints.post_controller.post_list_by_tag import PostListByTag
from endpoints.comment_controller.comment_get_list import CommentList
from endpoints.comment_controller.create_comment import CreateComment
from endpoints.comment_controller.delete_comment import DeleteComment
from endpoints.comment_controller.list_comment_by_user import ListCommentByUser
from endpoints.comment_controller.list_comment_by_post import ListCommentByPost
from endpoints.tag_controller.list_tags import TagsList


class BaseTest:
    get_user_list: UserList
    create_user: CreateUser
    update_user: UpdateUser
    get_user: UserGet
    delete_user: DeleteUser
    post_list: PostList
    create_post: CreatePost
    update_post: UpdatePost
    delete_post: DeletePost
    post_by_id: PostByID
    post_list_by_id_user: PostListByIDUser
    post_list_by_tag: PostListByTag
    comment_get_list: CommentList
    create_comment: CreateComment
    delete_comment: DeleteComment
    list_comment_by_user: ListCommentByUser
    list_comment_by_post: ListCommentByPost
    list_tags: TagsList

    @pytest.fixture(autouse=True)
    def setup(self, request):
        request.cls.get_user_list = UserList()
        request.cls.create_user = CreateUser()
        request.cls.update_user = UpdateUser()
        request.cls.get_user = UserGet()
        request.cls.delete_user = DeleteUser()
        request.cls.post_list = PostList()
        request.cls.create_post = CreatePost()
        request.cls.update_post = UpdatePost()
        request.cls.delete_post = DeletePost()
        request.cls.post_by_id = PostByID()
        request.cls.post_list_by_id_user = PostListByIDUser()
        request.cls.post_list_by_tag = PostListByTag()
        request.cls.comment_get_list = CommentList()
        request.cls.create_comment = CreateComment()
        request.cls.delete_comment = DeleteComment()
        request.cls.list_comment_by_user = ListCommentByUser()
        request.cls.list_comment_by_post = ListCommentByPost()
        request.cls.list_tags = TagsList()
