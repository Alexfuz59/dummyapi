import datetime as dt
import re
from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationInfo, HttpUrl
from enums.user_enums import Title, Genders
from pydantic.types import PastDate
from typing import Optional


class User(BaseModel):
    id: str
    title: Optional[Title] = None
    firstName: str = Field(min_length=2, max_length=52)
    lastName: str = Field(min_length=2, max_length=52)
    gender: Optional[Genders] = None
    email: EmailStr
    dateOfBirth: Optional[PastDate] = None
    registerDate: str
    updatedDate: str
    phone: Optional[str] = None
    picture: HttpUrl
    location: Optional[str] = None

    @field_validator('phone')
    def check_phone(cls, phone):
        pattern = r'((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}'
        phone_result = re.finditer(pattern, phone)
        if not phone_result:
            raise ValueError('Invalid phone number')

    @field_validator('dateOfBirth')
    def check_birthday(cls, dateOfBirth):
        birthday = dt.datetime.strptime(dateOfBirth, '%d.%m.%Y')
        old_datetime = dt.datetime.strptime("01.01.1900", '%d.%m.%Y')
        if birthday < old_datetime:
            raise ValueError('Incorrect birthdate')
        return dateOfBirth

    @field_validator('registerDate')
    def check_datetime_registration(cls, registerDate):
        current_time = dt.datetime.now()
        registerTime = registerDate.replace('T', ' ').replace('Z', '')
        registerTime = dt.datetime.strptime(registerTime, '%Y-%m-%d %H:%M:%S.%f')
        assert registerTime < current_time, 'Invalid user registration date'
        return registerDate

    @field_validator('updatedDate')
    def check_update_datetime(cls, updatedDate, info: ValidationInfo):
        registerTime = info.data['registerDate'].replace('T', ' ').replace('Z', '')
        registerTime = dt.datetime.strptime(registerTime, '%Y-%m-%d %H:%M:%S.%f')
        updatedTime = updatedDate.replace('T', ' ').replace('Z', '')
        updatedTime = dt.datetime.strptime(updatedTime, '%Y-%m-%d %H:%M:%S.%f')
        if registerTime > updatedTime:
            raise ValueError('Invalid user update date')
        return updatedDate