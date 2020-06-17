from django.test import TestCase
from ..management.commands.off_db import Command


class TestCommand(TestCase):
    """
    Tests the update of the purbeurre DB from OpenFoodFacts API.
    """

    def setup(self):
        self.command = Command()
        self.category = "category"
        self.product = {
            "name": "name",
            "link": "http://url.com",
            "nutriscore": "a",
            "category": self.category,
            "img": "http://img.com",
            "nutrition_img": ""
        }

    def test_handle(self):
        # mock request api et teste insertiopn en DB, mas ça c'est deja teste qd on teste les mmodels des prods ?
        pass
