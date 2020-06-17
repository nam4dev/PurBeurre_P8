#!/usr/bin/env python3
""" populating and updating purbeurre DB from openfoodfacts API."""

from django.core.management.base import BaseCommand
from purbeurre_off.models import Product, Category
import requests


# from django.core.management.base import CommandError
# from django.db import IntegrityError


class Command(BaseCommand):
    help = 'Update DB from OFF API'

    def handle(self, *args, **options):
        self.stdout.write('updating DB')
        Product.objects.all().delete()
        api_url = 'https://fr.openfoodfacts.org/categories&json=1'
        request_categories = requests.get(api_url)
        categories_json = request_categories.json()
        data_tags = categories_json.get('tags')
        # make some sorting and get products
        self.get_categories(data_tags)
        self.stdout.write(self.style.SUCCESS('DB successfully updated'))

    def sort_and_register_products(self, products, category, nb_prod):
        """
        Sorting products from the API to keep only those with useful information.
        And inserting selected products in the database.
        :param products: list of product from the API to be registered in the DB.
        :param category: the category instance to search for products in the API.
        :param nb_prod: number of products already registered in the DB.
        :return nb_prod: incremented nb_prod for each product added in the DB.
        """

        for product in products:
            url = product.get('url')
            name = product.get('product_name_fr')
            nutriscore = product.get('nutrition_grades')
            country = product.get('countries')
            img = product.get("image_url")
            nutrition_img = product.get("image_nutrition_small_url")
            if all([
                url,
                name and len(name) <= 100,
                nutriscore,
                country.lower().strip() == "france",
                img,
                nutrition_img
            ]):
                # insert product in DB
                Product.objects.get_or_create(
                    name=name,
                    link=url,
                    nutriscore=nutriscore.lower(),
                    category=category,
                    img=img,
                    nutrition_img=nutrition_img
                )

                nb_prod += 1

        return nb_prod

    def get_products(self, category, url, products_number):
        """
        Requesting products to the API, and then
        calling sort_and_register_products to sort and
        insert in the database retrieved products.
        :param category: the category instance to search for products in the API.
        :param url: url of the category
        :param products_number: number of products contained in this category.
        """

        pages_count = 1
        # 20 products / page
        needed_pages = products_number / 20
        nb_prod = 0
        while (pages_count < needed_pages) and (nb_prod < 500):
            # we request pages one by one, and we limit number of products for Heroku DB size
            request_products = requests.get(f'{url}/{str(pages_count)}.json')
            pages_count += 1
            products_json = request_products.json()
            products = products_json.get('products')
            nb_prod = self.sort_and_register_products(products, category, nb_prod)

        print(f'500 products inserted for {category.name} -> break')

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
                print(f'{category_selected} categories inserted in DB -> break')
                break
