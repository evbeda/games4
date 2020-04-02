import uuid
import hashlib


class InvalidEmailFormat(Exception):
    pass


class InvalidLoginUserPassword(Exception):
    pass


class InvalidLoginUserDisabled(Exception):
    pass


class EmailSender:
    def send_email(self, email, subject, content):
        print('PLEASE DONT SHOW ME!!!')
        print(email, subject, content)
        pass


def save_registration(first_name, last_name, email, hashed_password):
    print('PLEASE DONT SHOW ME!!!')


class User:
    def __init__(self, email=None, first_name=None, last_name=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name


def get_user(email, hashed_password):
    print('PLEASE DONT SHOW ME!!!')
    return User()


def register(first_name, last_name, email, password):
    if '@' not in email:
        raise InvalidEmailFormat()

    registrarion_token = str(uuid.uuid4())
    save_registration(first_name, last_name, email, hashlib.sha224(password.encode()).hexdigest())
    EmailSender().send_email(
        email,
        'Welcome {}'.format(first_name),
        'Please click here: domain/confirm.html?t={}'.format(
            registrarion_token,
        ),
    )

    return registrarion_token


def login(email, password):
    hashed_password = hashlib.sha224(password.encode()).hexdigest()
    logged_user = get_user(email, hashed_password)
    if not logged_user:
        raise InvalidLoginUserPassword()
    return logged_user
