from django.test import TestCase
from ..management.commands.off_db import Command


class TestCommand(TestCase):
    """
    Tests the update of the purbeurre DB from OpenFoodFacts API.
    """

    def setup(self):
        self.command = Command()
        self.category = ""
        self.product = {

        }

    def test_handle(self):
        pass