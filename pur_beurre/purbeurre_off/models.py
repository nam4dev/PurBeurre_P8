from django.db import models


class ProductManager(models.Manager):
    def search(self, query):
        # looking for the product
        product_searched = self.filter(name__iexact=query).first()
        # if product not found, looking for a product with a similar name
        if not product_searched:
            product_searched = self.filter(name__icontains=query).first()
        return product_searched

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
