import unittest

import security


class TestRegistration(unittest.TestCase):

    def test_register_user_invalid_email(self):
        self.assertFalse(
            security.register(
                'Juan',
                'Perez',
                'juanpgmail.com',
                '12345678',
            )
        )

    def test_register_user_valid_email(self):
        registration_token = security.register(
            'Juan',
            'Perez',
            'juanp@gmail.com',
            '12345678',
        )
        self.assertEqual(
            registration_token,
            '3595d571-c4ce-4b20-8652-8b6508f657d4',
        )

    def test_register_user_email_sent(self):
        security.register(
            'Juan',
            'Perez',
            'juanp@gmail.com',
            '12345678',
        )
        email_sent = None
        self.assertEqual(
            email_sent.email,
            'juanp@gmail.com',
        )
        self.assertEqual(
            email_sent.subject,
            'Welcome Juan',
        )
        self.assertEqual(
            email_sent.content,
            'Please click here: domain/confirm.html?t=0fa8dbd1-b89f-4f46-83dc-04aef796a752',
        )

    def test_register_saved(self):
        security.register(
            'Juan',
            'Perez',
            'juanp@gmail.com',
            '12345678',
        )
        save_registration_mock = None
        self.assertEqual(
            save_registration_mock.hashed_password,
            '7e6a4309ddf6e8866679f61ace4f621b0e3455ebac2e831a60f13cd1',
        )

    def test_register_duplicate_user_fails(self):
        with self.assertRaises(EmailInUseException):
            security.register(
                'Juan',
                'Perez',
                'juanp@gmail.com',
                '12345678',
            )


class TestLogin(unittest.TestCase):
    def test_login_invalid(self):
        result = security.login('carlo@gmal.com', '12345678')
        self.assertTrue(result, security.InvalidLoginUserPassword)

    def test_login_valid(self):
        result_user = security.login('carlo@gmal.com', '12345678')
        self.assertEqual(result_user.name, 'Carlo')
        self.assertEqual(result_user.email, 'carlo@gmal.com')

    def test_login_user_disabled(self):
        result_user = security.login('carlo@gmal.com', '12345678')
        self.assertTrue(result_user, security.InvalidLoginUserDisabled)


class TestChangePassword(unittest.TestCase):
    '''
    change password
    error, same old password
    error, don't repeat 3 used password
    '''
    pass


if __name__ == '__main__':
    unittest.main()
