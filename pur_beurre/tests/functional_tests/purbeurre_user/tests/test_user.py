from django.conf import settings
from selenium.webdriver.common.keys import Keys

from tests.functional_tests.func_tests import GeneralTestCase


class AccountTestCase(GeneralTestCase):

    def setUp(self):
        super().setUp()
        selenium = self.selenium
        # find the form element
        self.id_username = selenium.find_element_by_xpath('//label[@for="id_username"]')
        self.id_password = selenium.find_element_by_xpath('//label[@for="id_password"]')
        self.id_pwd_confirm = selenium.find_element_by_xpath('//label[@for="id_pwd_confirm"]')
        self.id_first_name = selenium.find_element_by_xpath('//label[@for="id_first_name"]')

        self.submit = selenium.find_element_by_by_xpath('//input[@type="submit"]')

    def test_create_account_ok(self):
        """
        Tests the user account creation with a valid form.
        """

        # Opening the link we want to test
        self.selenium.get('/user/create_account?')
        # Fill the form with data
        self.id_username.send_keys('create_account@selenium.com')
        self.id_password.send_keys('create_account')
        self.id_pwd_confirm.send_keys('create_account')
        self.id_first_name.send_keys('createaccount')

        # submitting the form
        self.submit.send_keys(Keys.RETURN)

        # check the returned result
        assert 'AHOY CREATEACCOUNT !' in self.selenium.page_source

    def test_create_account_diff_pwd(self):
        """
        Tests the user account creation,
        when the confirmation password is different from the first password.
        """

        # Opening the link we want to test
        self.selenium.get('/user/create_account?')
        # Fill the form with data
        self.id_username.send_keys('create_account_diff_pwd@selenium.com')
        self.id_password.send_keys('create_account_diff_pwd')
        self.id_pwd_confirm.send_keys('not_selenium_test')
        self.id_first_name.send_keys('createaccountdiffpwd')

        # submitting the form
        self.submit.send_keys(Keys.RETURN)

        # check the returned result
        assert 'veuillez entrer un mot de passe de confirmation identique au mot de passe' \
               ' choisi.' in self.selenium.page_source

    def test_connection_ok(self):
        """
        Tests the user connection with a valid form.
        """

        # Opening the link we want to test
        self.selenium.get('/user/connection')
        # Fill the form with data
        self.id_username.send_keys('connection@selenium.com')
        self.id_password.send_keys('connection')

        # submitting the form
        self.submit.send_keys(Keys.RETURN)

        # check the returned result
        assert 'Vous êtes connecté(e), Sélénium!' in self.selenium.page_source

    def test_connection_wrong_pwd(self):
        """
        Tests the user connection with a wrong password.
        """

        # Opening the link we want to test
        self.selenium.get('/user/connection')
        # Fill the form with data
        self.id_username.send_keys('connection@selenium.com')
        self.id_password.send_keys('not_selenium_test')

        # submitting the form
        self.submit.send_keys(Keys.RETURN)

        # check the returned result
        assert 'Utilisateur inconnu ou mauvais de mot de passe.' in self.selenium.page_source

    def test_connection_user_not_known(self):
        """
        Tests the user connection with a wrong password.
        """

        # Opening the link we want to test
        self.selenium.get('/user/connection')
        # Fill the form with data
        self.id_username.send_keys('user_not_known@test.com')
        self.id_password.send_keys('selenium_test')

        # submitting the form
        self.submit.send_keys(Keys.RETURN)

        # check the returned result
        assert 'Utilisateur inconnu ou mauvais de mot de passe.' in self.selenium.page_source

    # def test_welcome_page(self):
    #     # pdb.set_trace()
    #     # Create a session storage object.
    #     session_store = create_session_store()
    #     # In pdb, you can do 'session_store.session_key' to view the session key just created.
    #
    #     # Create a session object from the session store object.
    #     session_items = session_store
    #
    #     # Add a session key/value pair.
    #     session_items['uid'] = 1
    #     session_items.save()
    #
    #     # Go to the correct domain.
    #     self.selenium.get(self.live_server_url)
    #
    #     # Add the session key to the cookie that will be sent back to the server.
    #     self.selenium.add_cookie({'name': settings.SESSION_COOKIE_NAME, 'value': session_store.session_key})
    #     # In pdb, do 'self.selenium.get_cookies() to verify that it's there.'
    #
    #     # The client sends a request to the view that's expecting the session item.
    #     self.selenium.get(self.live_server_url + '/signup/')
    #     body = self.selenium.find_element_by_tag_name('body')
    #     self.assertIn('Welcome', body.text)
