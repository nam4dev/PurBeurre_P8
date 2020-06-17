from django.test import TestCase
from django.urls import reverse


# Create your tests here.
# test home
class TestHome(TestCase):
    """
    Home app views test.
    """
    def test_home(self):
        """
        Getting the home page should return a http code = 200.
        """
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('purbeurre_home/home.html')

    def test_legal(self):
        """
        Getting the legal notice page should return a http code = 200.
        """

        response = self.client.get(reverse('legal'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('purbeurre_home/legal_notices.html')
