from django.test import LiveServerTestCase
from selenium import webdriver


class GeneralTestCase(LiveServerTestCase):
    """
    Parent class to setup the selenium tests.
    """

    def setUp(self):
        self.selenium = webdriver.Chrome('functional_tests/chromedriver.exe')
        super(GeneralTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(GeneralTestCase, self).tearDown()
