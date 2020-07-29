from tests.functional_tests.func_tests import GeneralTestCase


class AccountTestCase(GeneralTestCase):

    def setUp(self):
        super().setUp()

        self.create_url = 'http://127.0.0.1:8000/user/create_account?'
        self.connect_url = 'http://127.0.0.1:8000/user/connection'

    def account_basis(self, url):
        """
        Common settings depending on the page we want (create account or connection).

        :param url: url of the page we want.
        :return username, password, pwd_confirm, first_name, submit: form elements found.
        when using connection url, pwd_confirm and first_name not found
        -> replaced by an empty string.
        """

        # Opening the link we want to test
        self.selenium.get(url)

        # find the form element
        username = self.selenium.find_element_by_name("username")
        password = self.selenium.find_element_by_name("password")
        try:
            pwd_confirm = self.selenium.find_element_by_name("pwd_confirm")
            first_name = self.selenium.find_element_by_name("first_name")
        except:
            pwd_confirm = ""
            first_name = ""

        submit = self.selenium.find_element_by_xpath('//input[@type="submit"]')

        return username, password, pwd_confirm, first_name, submit

    def test_create_account_ok(self):
        """
        Tests the user account creation with a valid form.
        """

        username, password, pwd_confirm, first_name, submit = self.account_basis(self.create_url)

        # Fill the form with data
        username.send_keys('create_account9@selenium.com')
        password.send_keys('create_account')
        pwd_confirm.send_keys('create_account')
        first_name.send_keys('createaccount')

        # submitting the form
        submit.click()
        self.wait

        # check the returned result
        self.assertEqual(
            self.selenium.current_url,
            'http://127.0.0.1:8000/user/my_account',
            "urlfound: " + self.selenium.current_url
        )
        assert "AHOY CREATEACCOUNT" in self.selenium.page_source

    def test_create_account_diff_pwd(self):
        """
        Tests the user account creation,
        when the confirmation password is different from the first password.
        """

        username, password, pwd_confirm, first_name, submit = self.account_basis(self.create_url)

        # Fill the form with data
        username.send_keys('create_account_diff_pwd@selenium.com')
        password.send_keys('create_account_diff_pwd')
        pwd_confirm.send_keys('not_selenium_test')
        first_name.send_keys('createaccountdiffpwd')

        # submitting the form
        submit.click()
        self.wait

        # check the returned result
        assert 'veuillez entrer un mot de passe de confirmation identique' in self.selenium.page_source

    def test_connection_wrong_pwd(self):
        """
        Tests the user connection with a wrong password.
        """

        username, password, pwd_confirm, first_name, submit = self.account_basis(self.connect_url)

        # Fill the form with data
        username.send_keys('connection@selenium.com')
        password.send_keys('not_selenium_test')

        # submitting the form
        submit.click()
        self.wait

        # check the returned result
        assert 'Utilisateur inconnu ou mauvais de mot de passe.' in self.selenium.page_source

    def test_connection_user_not_known(self):
        """
        Tests the user connection with a wrong password.
        """

        username, password, pwd_confirm, first_name, submit = self.account_basis(self.connect_url)

        # Fill the form with data
        username.send_keys('user_not_known@test.com')
        password.send_keys('selenium_test')

        # submitting the form
        submit.click()
        self.wait

        # check the returned result
        assert 'Utilisateur inconnu ou mauvais de mot de passe.' in self.selenium.page_source

    def test_connection_ok(self):
        """
        Tests the user connection with a valid form.
        """

        username, password, pwd_confirm, first_name, submit = self.account_basis(self.connect_url)

        # Fill the form with data
        username.send_keys('connection@selenium.com')
        password.send_keys('connection')

        # submitting the form
        submit.click()
        self.wait

        # check the returned result
        assert 'Vous êtes connecté(e), Sélénium !' in self.selenium.page_source
        self.assertEqual(
            self.selenium.current_url,
            'http://127.0.0.1:8000/user/connection',
            "urlfound: " + self.selenium.current_url
        )
