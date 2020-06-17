from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class TestFavoritesViews(TestCase):
    """
    Favorites app views test.
    """
    def setUp(self):
        self.username = 'moi@gmail.com'
        self.password = 'moi'
        self.client.login(username=self.username, password=self.password)

    def test_favorites_favorites(self):
        """
        Getting the favorites page should return a http code = 200.
        """
        response = self.client.get(reverse('favorites'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('purbeurre_favorites/favorites.html')

    def test_favorites_save(self):
        pass

    def test_favorites_remove(self):
        pass
