from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase, Client

from purbeurre_user.forms import ConnectionForm, AccountForm


# Create your tests here.
class TestUserForms(TestCase):
    """
    User app forms test.
    """
    def setUp(self):
        self.username = 'moi@gmail.com'
        self.password = 'moi'
        self.pwd_confirm = 'me'
        self.client = Client()
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.data = {
            'username': self.username,
            'password': self.password,
            'pwd_confirm': self.pwd_confirm
        }

    def test_user_account_form_same_username(self):
        self.assertRaises(ValidationError, AccountForm.clean_username, self)

    def test_user_account_form_wrong_confirm_pwd(self):
        self.assertRaises(ValidationError, AccountForm.clean_pwd_confirm, self)