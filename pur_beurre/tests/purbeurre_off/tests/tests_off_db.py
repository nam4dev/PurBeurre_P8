from django.test import TestCase
import unittest.mock as mock
from purbeurre_off.management.commands.off_db import Command
from purbeurre_off.models import Product


class TestCommand(TestCase):
    """
    Tests the update of the purbeurre DB from OpenFoodFacts API.
    """

    def setUp(self):
        self.command = Command()
        self.category = "category"
        self.product = {
            "name": "name",
            "link": "http://url.com",
            "nutriscore": "a",
            "category": self.category,
            "img": "http://img.com",
            "nutrition_img": "http://img.com"
        }

    def test_sort_and_register_products(self):
        products = [
                {
                    'url': self.product['link'],
                    'product_name_fr': self.product['name'],
                    'nutrition_grades': self.product['nutriscore'],
                    'countries': "france",
                    'image_url': self.product['img'],
                    'image_nutrition_small_url': self.product['nutrition_img']
                }
            ]
        # calling function
        result = self.command.sort_and_register_products(
            products,
            self.category,
            nb_prod=0
        )
        # expected result
        self.assertEqual(result, 1)
        self.assertEqual(Product.objects.all().exists(), True)

    # @mock.patch('sort_and_register_products')
    # @mock.patch('requests.get')
    # def test_get_products(self):
    #     pass

    # @mock.patch('get_products')
    # def test_get_categories(self):
    #     pass
    #
    # def _setup_mocked_response(self, response, ok_status=True):
    #     mocked_response = mock.Mock(ok=ok_status)
    #     mocked_response.json.return_value = response
    #     return mocked_response
    #
    # @mock.patch('get_categories')
    # @mock.patch('requests.get')
    # def test_handle(
    #         self,
    #         mocked_request_get,
    #         mocked_categories_json_get,
    #         mocked_get_categories
    # ):
    #     # mock request api et teste insertiopn en DB, mas ça c'est deja teste qd on teste les mmodels des prods ?
    #     self.command
    #     pass
