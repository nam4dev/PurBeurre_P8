from django.test import TestCase
from django.db import models

from purbeurre_off.models import Category, Product, ProductManager


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
        self.category = Category.objects.create(name="category")
        Product.objects.create(
            name="name",
            link="http://url.com",
            nutriscore="a",
            category=self.category,
            img="http://img.com",
            nutrition_img=""
        )

    # def test_models_columns(self):
        # self.assertIsInstance(self.model.name, Product)
        # self.assertIsInstance(self.model.link, models.URLField)
        # self.assertIsInstance(self.model.nutriscore, models.CharField)
        # self.assertIsInstance(self.model.category, models.ForeignKey)
        # self.assertIsInstance(self.model.img, models.URLField)
        # self.assertIsInstance(self.model.nutrition_img, models.URLField)

    def test_product_objects(self):
        self.assertIsInstance(Product.objects, ProductManager)

    def test_product_columns(self):
        product = Product.objects.get(name="name")
        self.assertEqual("name", product.name)
        self.assertEqual("http://url.com", product.link)
        self.assertEqual("a", product.nutriscore)
        self.assertEqual(self.category, product.category)
        self.assertEqual("http://img.com", product.img)
        self.assertEqual("", product.nutrition_img)


class TestProductIntegration(TestCase):
    pass


class TestCategory(TestCase):
    """
    Tests product creation in DB.
    """

    def setUp(self):
        self.category = Category.objects.create(name="category")
        self.model = Category(self.category)

    def test_category_objects(self):
        self.assertIsInstance(self.category, Category)

    def test_category_columns(self):
        self.assertEqual("category", self.category.name)


class TestCategoryIntegration(TestCase):
    pass
