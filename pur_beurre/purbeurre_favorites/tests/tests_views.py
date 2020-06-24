from django.contrib.auth.models import User
from django.contrib.auth import login
from django.test import TestCase, Client
from django.urls import reverse

from purbeurre_favorites.models import Favorite
from purbeurre_off.models import Product, Category


# Create your tests here.
class TestFavoritesViews(TestCase):
    """
    Favorites app views test.
    """
    def setUp(self):
        self.username = 'moi@gmail.com'
        self.password = 'moi'
        self.client = Client()
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)
        self.category = Category.objects.create(name="category")
        self.product = Product.objects.create(
            name="name",
            link="http://url.com",
            nutriscore="a",
            category=self.category,
            img="http://img.com",
            nutrition_img=""
        )
        self.favorite = Favorite.objects.create(user=self.user, favorite=self.product)

    def test_favorites_favorites(self):
        """
        Getting the favorites page should return a http code = 200.
        """
        response = self.client.get(reverse('favorites'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('purbeurre_favorites/favorites.html')

    def test_favorites_save(self):
        response = self.client.get(reverse('save'), {'product': self.product.id})
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('purbeurre_favorites/favorites.html')

    def test_favorites_remove(self):
        response = self.client.post(reverse('remove',), {'product': self.favorite.id})
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('purbeurre_favorites/favorites.html')
