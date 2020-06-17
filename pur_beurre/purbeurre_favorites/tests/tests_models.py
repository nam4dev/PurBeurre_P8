from django.test import TestCase
import unittest
from django.conf import settings
import os
import django
from django.db import models
from ..models import Favorite
from ..models import FavoriteManager


# Create your tests here.
class TestFavorite(TestCase):
# class TestFavorite(unittest.TestCase):
    """
    Tests favorite creation in DB.
    """

    def setUp(self):
        # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pur_beurre.settings')
        # django.setup()
        self.model = Favorite()

    def test_models_columns(self):
        self.assertIsInstance(self.model.user, models.ForeignKey)
        self.assertIsInstance(self.model.favorite, models.ForeignKey)

    def test_favorite_objects(self):
        self.assertIsInstance(self.model.objects, FavoriteManager)


class TestFavoriteIntegration(TestCase):
    pass
