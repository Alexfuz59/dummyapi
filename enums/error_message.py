from enum import Enum


class ErrorMessage(Enum):
    ERROR_STATUS_CODE = lambda status_code: f'Error status code {status_code}'
    ERROR_USER_ID_COMMENT = 'Invalid user ID in comment'
    ERROR_POST_ID_COMMENT = 'Invalid post ID in comment'
    ERROR_POST_ID_COMMENT_LIST = 'Invalid post ID in comment list'
    ERROR_USER_ID_COMMENT_LIST = 'Invalid user ID in comment list'
    ERROR_POST_ID_SEARCH = 'Invalid search by post id'
    ERROR_UPDATE_TEXT = 'Error text update'
    ERROR_UPDATE_IMAGE = 'Error image update'
    ERROR_UPDATE_LINK = 'Error link update'
    ERROR_UPDATE_TAGS = 'Error tags update'
    ERROR_FIRSTNAME_UPDATED = 'FirstName has not been updated'
    ERROR_LASTNAME_UPDATED = 'LastName has not been updated'
    ERROR_TOTAL_OBJECTS = 'Wrong total number of objects'
    ERROR_VALIDATION = 'Response validation error'
