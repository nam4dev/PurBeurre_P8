from django.test import LiveServerTestCase
from selenium import webdriver


# search test
class GeneralTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        super(GeneralTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(GeneralTestCase, self).tearDown()
    # puis des fichiers différents pour les diff apps ( favorite save, ...)