from importlib import import_module

from django.test import LiveServerTestCase
from selenium import webdriver
from django.conf import settings

#
# def create_session_store():
#     """ Creates a session storage object. """
#
#     # from django.utils.importlib import import_module
#     engine = import_module(settings.SESSION_ENGINE)
#     # Implement a database session store object that will contain the session key.
#     store = engine.SessionStore()
#     store.save()
#     return store


class GeneralTestCase(LiveServerTestCase):
    """
    Parent class to setup the selenium tests.
    """
    selenium = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        profile = webdriver.FirefoxProfile()
        cls.selenium = webdriver.Firefox(firefox_profile=profile, executable_path=r'.\tests\functional_tests\geckodriver.exe')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()


    # def setUp(self):
    #     super(GeneralTestCase, self).setUp()
    #     self.selenium = webdriver.Chrome(executable_path=r'.\tests\functional_tests\chromedriver.exe')
    #     self.selenium.implicitly_wait(3)
    #
    # def tearDown(self):
    #     super(GeneralTestCase, self).tearDown()
    #     self.selenium.implicitly_wait(3)
    #     self.selenium.quit()

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
