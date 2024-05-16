from faker import Faker
from random import randint

fake = Faker()
fake_ru = Faker('ru_RU')


class RegisterUser:
    @staticmethod
    def user_data():
        firstName = fake.first_name()
        lastName = fake.last_name()
        email = fake.ascii_free_email()
        picture = fake.image_url()
        phone = fake_ru.phone_number()
        return {"firstName": firstName,
                "lastName": lastName,
                "email": email,
                "phone": phone,
                "picture": picture
                }


class UpdateUserDate:
    @staticmethod
    def data_update():
        firstName = fake.first_name()
        lastName = fake.last_name()
        picture = fake.image_url()
        return {"firstName": firstName,
                "lastName": lastName,
                "picture": picture
                }

    @staticmethod
    def update_email():
        email = fake.ascii_free_email()
        return {
                "email": email
                }


class RegisterPost:
    @staticmethod
    def post_data(owner_id):
        text = fake.text(max_nb_chars=20)
        image = fake.image_url()
        likes = randint(0, 1000)
        tags = fake.word()
        owner = owner_id
        return {"text": text,
                "image": image,
                "likes": likes,
                "tags": tags,
                "owner": owner
                }


class UpdatePostDate:
    @staticmethod
    def update_post():
        text = fake.text(max_nb_chars=50)
        image = fake.image_url()
        link = fake.uri()
        tags = fake.word()
        return {"text": text,
                "image": image,
                "link": link,
                "tags": tags
                }


class CreateCommentDate:
    @staticmethod
    def data_comment(owner_id, post_id):
        message = fake.text(max_nb_chars=70)
        owner = owner_id
        post = post_id
        return {"owner": owner,
                "post": post,
                "message": message
                }
