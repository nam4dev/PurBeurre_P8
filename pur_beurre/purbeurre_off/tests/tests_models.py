from django.test import TestCase
from django.db import models

from ..models import Category, Product, ProductManager


# # Create your tests here.
# class TestCategory(TestCase):
#     """
#     Tests category creation in DB.
#     """
#
#     def setUp(self):
#         Category.objects.create(name="category_test")
#
#     def test_category(self):
#         category = Category.objects.get(name="category_test")
#         self.assertEqual("category_test", category.name)
#
#
# class TestProduct(TestCase):
#     """
#     Tests Product creation in DB.
#     """
#     def setUp(self):
#         Product.object.create(
#             name="product_name",
#             link="link_url",
#             nutriscore="product_nutriscore",
#             category="product_category",
#             img="product_img",
#             nutrition_img="product_nutrition_img"
#         )
#
#     def test_product(self):
#         product = Product.objects.get(name="product_name")
#         self.assertEqual("product_name", product.name)


# Create your tests here.
class TestProduct(TestCase):
    """
    Tests product creation in DB.
    """

    def setUp(self):
        # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pur_beurre.settings')
        # django.setup()
        self.model = Product()

    def test_models_columns(self):
        self.assertIsInstance(self.model.name, models.CharField)
        self.assertIsInstance(self.model.link, models.URLField)
        self.assertIsInstance(self.model.nutriscore, models.CharField)
        self.assertIsInstance(self.model.category, models.ForeignKey)
        self.assertIsInstance(self.model.img, models.URLField)
        self.assertIsInstance(self.model.nutrition_img, models.URLField)

    def test_product_objects(self):
        self.assertIsInstance(self.model.objects, ProductManager)


class TestProductIntegration(TestCase):
    pass


class TestCategory(TestCase):
    """
    Tests product creation in DB.
    """

    def setUp(self):
        # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pur_beurre.settings')
        # django.setup()
        self.model = Category()

    def test_models_columns(self):
        self.assertIsInstance(self.model.name, models.CharField)


class TestCategoryIntegration(TestCase):
    pass
