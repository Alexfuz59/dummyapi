from faker import Faker
from random import randint

fake = Faker()


class RegisterUser:
    @staticmethod
    def user_data():
        firstName = fake.first_name()
        lastName = fake.last_name()
        email = fake.ascii_free_email()
        picture = fake.image_url()
        return {"firstName": firstName,
                "lastName": lastName,
                "email": email,
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
    def post_data():
        text = fake.text(max_nb_chars=20)
        image = fake.image_url()
        likes = randint(0, 1000)
        tags = fake.word()
        return {"text": text,
                "image": image,
                "likes": likes,
                "tags": tags
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
    def data_comment():
        message = fake.text(max_nb_chars=70)
        return {"message": message}
