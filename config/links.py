BASE_URL = 'https://dummyapi.io/data/v1'


class UserDataLink:
    GET_LIST = f'{BASE_URL}/user'
    GET_USER_BY_ID = lambda self, user_id: f'{BASE_URL}/user/{user_id}'
    CREATE_USER = f'{BASE_URL}/user/create'
    UPDATE_USER = lambda self, user_id: f'{BASE_URL}/user/{user_id}'
    DELETE_USER = lambda self, user_id: f'{BASE_URL}/user/{user_id}'


class PostDataLink:
    GET_LIST_POST = f'{BASE_URL}/post'
    GET_LIST_BY_USER = lambda self, user_id: f'{BASE_URL}/user/{user_id}/post'
    GET_POST_BY_ID = lambda self, post_id: f'{BASE_URL}/post/{post_id}'
    GET_LIST_BY_TAG = lambda self, user_id: f'{BASE_URL}/tag/{user_id}/post'
    CREATE_POST = f'{BASE_URL}/post/create'
    UPDATE_POST = lambda self, post_id: f'{BASE_URL}/post/{post_id}'
    DELETE_POST = lambda self, post_id: f'{BASE_URL}/post/{post_id}'


class CommentDataLink:
    GET_LIST_COMMENT = f'{BASE_URL}/comment'
    GET_LIST_COMMENT_BY_POST = lambda self, post_id: f'{BASE_URL}/post/{post_id}/comment'
    GET_LIST_COMMENT_BY_USER = lambda self, user_id:  f'{BASE_URL}/user/{user_id}/comment'
    CREATE_COMMENT = f'{BASE_URL}/comment/create'
    DELETE_COMMENT = lambda self, comment_id: f'{BASE_URL}/comment/{comment_id}'


class TagsDataLink:
    GET_LIST_TAGS = f'{BASE_URL}/tag'
