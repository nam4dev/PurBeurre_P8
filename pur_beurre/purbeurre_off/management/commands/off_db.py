#!/usr/bin/env python3
""" populating and updating purbeurre DB from openfoodfacts API."""

from django.core.management.base import BaseCommand
from purbeurre_off.models import Product, Category
import requests
# from django.core.management.base import CommandError
# from django.db import IntegrityError


class Command(BaseCommand):
    help = 'Update DB from OFF API'

    # def add_arguments(self, parser):
    #     # parser.add_argument('poll_ids', nargs='+', type=int)
    #     pass

    def handle(self, *args, **options):
        self.stdout.write('updating DB')
        api_url = 'https://fr.openfoodfacts.org/categories&json=1'
        request_categories = requests.get(api_url)
        categories_json = request_categories.json()
        data_tags = categories_json.get('tags')
        # make some sorting and get products
        self.get_categories(data_tags)
        self.stdout.write(self.style.SUCCESS('DB successfully updated'))

    def sort_and_register_products(self, products, category):
        """
        Sorting products from the API to keep only those with useful information.
        And inserting selected products in the database.
        :param products: list of products from the API.
        :param category: the category instance to search for products in the API.
        """
        print("nb prods" + str(len(products)))
        for i in (range(0, len(products) - 1)):
            for product in products[i]:
                url = product.get('url')
                name = product.get('product_name_fr')
                nutriscore = product.get('nutrition_grades')
                country = product.get('countries')
                img = product.get("image_small_url")
                if all([
                    url,
                    name,
                    nutriscore,
                    country.lower().strip() == "france",
                    img
                ]):
                    # insert product in DB
                    Product.objects.get_or_create(
                        name=name,
                        link=url,
                        nutriscore=nutriscore,
                        category=category,
                        img=img)

    def get_products(self, category, url, products_number):
        """
        Requesting products to the API, and then
        calling sort_and_register_products to sort and
        insert in the database retrieved products.
        :param category: the category instance to search for products in the API.
        :param url: url of the category
        :param products_number: number of products contained in this category.
        """

        products = []
        pages_count = 1
        # needed_pages = products_number / 20
        # # if we take too many pages, it's too big for Heroku DB
        # if needed_pages > 50:
        #     needed_pages = 50
        #     print("needed pages" + str(needed_pages))
        needed_pages = 250

        while pages_count < needed_pages:
            # we request pages one by one
            # '&json=1&page_size=250'
            #'&json=' + str(pages_count)
            request_products = requests.get(url + '&json=' + str(pages_count))
            products_json = request_products.json()

            products.append(products_json.get('products'))
            pages_count += 1
        self.sort_and_register_products(products, category)

    def get_categories(self, data_tags):
        """
        Checking basic information from data_tags, insert categories into database
        and calling get_products to get products of the selected categories
        from the API.
        :param data_tags: categories information retrieved from the API.
        """

        category_selected = 0
        for idx, data in enumerate(data_tags):
            name = data['name']
            products_number = data['products']
            # for a useful category, we want at least 1000 products
            if products_number > 1000:
                if ":" not in name and "-" not in name:
                    # save category in DB
                    category, _ = Category.objects.get_or_create(name=name)
                    # get products for this category
                    self.get_products(category, data['url'], products_number)
                    category_selected += 1

            if category_selected == 15:
                break
