from selenium.webdriver.common.keys import Keys

from tests.functional_tests.func_tests import GeneralTestCase


class HomeTestCase(GeneralTestCase):

    def setUp(self):
        GeneralTestCase.setUp(self)
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('/home')
        # find the form element a completer
        self.search = selenium.find_element_by_xpath('//input[@placeholder="Chercher"]')
        self.prod = selenium.find_element_by_xpath('//input[@placeholder="Produit"]')
        self.submit = selenium.find_element_by_xpath('//button[@type="submit"]')

    def test_search_from_navbar_ok(self):
        """
        Tests the food search from the navbar with a product known to be registered in the DB.
        """

        # Fill the form with data
        self.search.send_keys('pain')

        # submitting the form
        self.search.send_keys(Keys.RETURN)

        # check the returned result
        assert 'a remplir' in self.selenium.page_source

    def test_search_from_navbar_prod_not_found(self):
        """
        Tests the food search from the navbar with a product known not to be registered in the DB.
        """

        # Fill the form with data
        self.search.send_keys('ftmpd654tedsgfra')

        # submitting the form
        self.search.send_keys(Keys.RETURN)

        # check the returned result
        assert 'a remplir' in self.selenium.page_source

    def test_search_from_homepage_ok(self):
        """
        Tests the food search from the body with a product known to be registered in the DB.
        """

        # Fill the form with data
        self.prod.send_keys('pain')

        # submitting the form
        self.submit.send_keys(Keys.RETURN)

        # check the returned result
        assert 'a remplir' in self.selenium.page_source

    def test_search_from_homepage_prod_not_found(self):
        """
        Tests the food search from the body with a product known not to be registered in the DB.
        """

        # Fill the form with data
        self.prod.send_keys('ftmpd654tedsgfra')

        # submitting the form
        self.submit.send_keys(Keys.RETURN)

        # check the returned result
        assert 'a remplir' in self.selenium.page_source
