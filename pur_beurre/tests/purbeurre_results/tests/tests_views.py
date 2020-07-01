from django.contrib.auth.models import User
from django.contrib.auth import login
from django.test import TestCase, Client
from django.urls import reverse

from purbeurre_favorites.models import Favorite
from purbeurre_off.models import Product, Category


# Create your tests here.
class TestResultsViews(TestCase):
    """
    Results app views test.
    """
    def setUp(self):

        self.category = Category.objects.create(name="category")
        self.product = Product.objects.create(
            name="name",
            link="http://url.com",
            nutriscore="a",
            category=self.category,
            img="http://img.com",
            nutrition_img=""
        )

    def test_results_results(self):
        """
        Getting the favorites page should return a http code = 200.
        """
        response = self.client.get(reverse('results'), {'query': 'name'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('purbeurre_results/results.html')

    def test_results_detail(self):
        response = self.client.get(reverse('detail', kwargs={'product_id': self.product.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('purbeurre_results/detail.html')

    def test_results_prod_not_found(self):
        response = self.client.get(reverse('results'), {'query': 'error'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('purbeurre_results/prod_not_found.html')
