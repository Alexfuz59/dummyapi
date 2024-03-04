BASE_URL = 'https://dummyapi.io/data/v1'


class UserDataLink:
    GET_LIST = f'{BASE_URL}/user'
    GET_USER_BY_ID = f'{BASE_URL}/user/'
    CREATE_USER = f'{BASE_URL}/user/create'
    UPDATE_USER = f'{BASE_URL}/user'
    DELETE_USER = f'{BASE_URL}/user'


class PostDataLink:
    GET_LIST_POST = f'{BASE_URL}/post'
    GET_LIST_BY_USER = f'{BASE_URL}/user'
    GET_POST_BY_ID = f'{BASE_URL}/post'
    GET_LIST_BY_TAG = f'{BASE_URL}/tag'
    CREATE_POST = f'{BASE_URL}/post/create'
    UPDATE_POST = f'{BASE_URL}/post'
    DELETE_POST = f'{BASE_URL}/post'


class CommentDataLink:
    GET_LIST_COMMENT = f'{BASE_URL}/comment'
    GET_LIST_COMMENT_BY_POST = f'{BASE_URL}/post'
    GET_LIST_COMMENT_BY_USER = f'{BASE_URL}/user'
    CREATE_COMMENT = f'{BASE_URL}/comment/create'
    DELETE_COMMENT = f'{BASE_URL}/comment'


class TagsDataLink:
    GET_LIST_TAGS = f'{BASE_URL}/tag'
