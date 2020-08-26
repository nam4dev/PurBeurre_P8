from django.test import LiveServerTestCase
from selenium import webdriver
import selenium.webdriver.support.ui as ui


class GeneralTestCase(LiveServerTestCase):
    """
    Parent class to setup the selenium tests.
    """
    selenium = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        profile = webdriver.FirefoxProfile()
        cls.selenium = webdriver.Firefox(
            firefox_profile=profile,
            executable_path=r'.\tests\functional_tests\geckodriver.exe'
        )
        cls.wait = ui.WebDriverWait(cls.selenium, 3)
        cls.wait_second = lambda sec=3: ui.WebDriverWait(cls.selenium, sec)
        cls.selenium.set_page_load_timeout(30)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
