from django.db import models


class ProductManager(models.Manager):

    def search(self, query):
        """
        Search the first product which matches the given query and associated substitutes

        Notes:
            Returns the substitutes as well if given parameter is set

        Args:
            query (str): The query terms

        Returns:
            tuple[list[Product], Product]: The first matched product with or without substitutes
        """
        substitutes = []
        first_product_found = None
        if query:
            # looking for the product
            products_found = self.filter((
                models.Q(name__iexact=query) | models.Q(name__icontains=query)
            ))
            if products_found:
                first_product_found = products_found.first()
                substitutes = products_found.filter(
                    category=first_product_found.category,
                    nutriscore__lt=first_product_found.nutriscore
                )
        return substitutes, first_product_found

    def search_favorite(self, product):
        favorite_prod = self.filter(id__exact=product).first()
        return favorite_prod


class Category(models.Model):
    """
    Class building categories and managing their interactions
    with other objects.
    """
    class Meta:
        verbose_name_plural = 'categories'
        app_label = 'purbeurre_off'

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    """
    Class building products and managing their interactions with other objects.
    """

    class Meta:
        unique_together = ('link', 'category',)

    objects = ProductManager()

    link = models.URLField()
    name = models.CharField(max_length=100)
    nutriscore = models.CharField(max_length=1)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    img = models.URLField()
    nutrition_img = models.URLField(null=True, blank=True)
