# from selenium.webdriver.common.keys import Keys
#
# from tests.functional_tests.func_tests import GeneralTestCase
#
#
# class FavoritesTestCase(GeneralTestCase):
#
#     def setUp(self):
#         GeneralTestCase.setUp(self)
#         selenium = self.selenium
#         # find the page element
#         self.detail = selenium.find_element_by_xpath('//label[@for="id_username"]')  ###
#         ###self.detail = selenium.find_element_by_xpath('//label[@for="id_username"]')  ###
#         ### a faire
#
#     def test_create_account_ok(self):
#         """
#         Tests the user account creation with a valid form.
#         """
#
#         # Opening the link we want to test
#         self.selenium.get('http://127.0.0.1:8000/user/create_account?')
#         # Fill the form with data
#         self.id_username.send_keys('create_account@selenium.com')
#         self.id_password.send_keys('create_account')
#         self.id_pwd_confirm.send_keys('create_account')
#         self.id_first_name.send_keys('createaccount')
#
#         # submitting the form
#         self.submit.send_keys(Keys.RETURN)
#
#         # check the returned result
#         assert 'AHOY CREATEACCOUNT !' in self.selenium.page_source
#
#     def test_create_account_diff_pwd(self):
#         """
#         Tests the user account creation,
#         when the confirmation password is different from the first password.
#         """
#
#         # Opening the link we want to test
#         self.selenium.get('http://127.0.0.1:8000/user/create_account?')
#         # Fill the form with data
#         self.id_username.send_keys('create_account_diff_pwd@selenium.com')
#         self.id_password.send_keys('create_account_diff_pwd')
#         self.id_pwd_confirm.send_keys('not_selenium_test')
#         self.id_first_name.send_keys('createaccountdiffpwd')
#
#         # submitting the form
#         self.submit.send_keys(Keys.RETURN)
#
#         # check the returned result
#         assert 'veuillez entrer un mot de passe de confirmation identique au mot de passe' \
#                ' choisi.' in self.selenium.page_source
#
#     def test_connection_ok(self):
#         """
#         Tests the user connection with a valid form.
#         """
#
#         # Opening the link we want to test
#         self.selenium.get('http://127.0.0.1:8000/user/connection')
#         # Fill the form with data
#         self.id_username.send_keys('connection@selenium.com')
#         self.id_password.send_keys('connection')
#
#         # submitting the form
#         self.submit.send_keys(Keys.RETURN)
#
#         # check the returned result
#         assert 'Vous êtes connecté(e), !' in self.selenium.page_source
#
#     def test_connection_wrong_pwd(self):
#         """
#         Tests the user connection with a wrong password.
#         """
#
#         # Opening the link we want to test
#         self.selenium.get('http://127.0.0.1:8000/user/connection')
#         # Fill the form with data
#         self.id_username.send_keys('connection@selenium.com')
#         self.id_password.send_keys('not_selenium_test')
#
#         # submitting the form
#         self.submit.send_keys(Keys.RETURN)
#
#         # check the returned result
#         assert 'Utilisateur inconnu ou mauvais de mot de passe.' in self.selenium.page_source
#
#     def test_connection_user_not_known(self):
#         """
#         Tests the user connection with a wrong password.
#         """
#
#         # Opening the link we want to test
#         self.selenium.get('http://127.0.0.1:8000/user/connection')
#         # Fill the form with data
#         self.id_username.send_keys('user_not_known@test.com')
#         self.id_password.send_keys('selenium_test')
#
#         # submitting the form
#         self.submit.send_keys(Keys.RETURN)
#
#         # check the returned result
#         assert 'Utilisateur inconnu ou mauvais de mot de passe.' in self.selenium.page_source
