from selenium.webdriver.common.keys import Keys
from django.test import Client
from tests.functional_tests.func_tests import GeneralTestCase


class FavoritesTestCase(GeneralTestCase):

    def setUp(self):
        super().setUp()

        # connect user
        client = Client()
        client.login(username='connection@selenium.com', password='connection')

    def test_save_as_favorite(self):
        """
        Tests the registration of a product as user's favorite.
        """
        # Opening the link we want to test
        self.selenium.get('http://127.0.0.1:8000/results/results?query=pain')
        # Click on "sauvegarder"
        save_product = self.selenium.find_element_by_xpath('//input[@value="Sauvegarder"]')
        save_product.click()
        self.wait

        # check the returned result
        self.assertEqual(
            self.selenium.current_url,
            'http://127.0.0.1:8000/favorites/favorites',
            "urlfound: " + self.selenium.current_url
        )
        assert 'MES ALIMENTS' in self.selenium.page_source

    def test_remove_from_favorites(self):
        """
        Tests the suppression of a favorite by the user.
        """

        # Opening the link we want to test
        self.selenium.get('http://127.0.0.1:8000/favorites/favorites')

        # Click on "Supprimer"
        delete_product = self.selenium.find_element_by_xpath('//input[@value="Supprimer"]')
        delete_product.click()
        self.wait

#         # check the returned result
# comment je fais là ??
#         assert 'veuillez entrer un mot de passe de confirmation identique au mot de passe' \
#                ' choisi.' in self.selenium.page_source
