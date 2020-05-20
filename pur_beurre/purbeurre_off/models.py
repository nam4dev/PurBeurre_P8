from django.db import models


class Category(models.Model):
    """
    Class building categories and managing their interactions
    with other objects.
    """
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    """
    Class building products and managing their interactions with other objects.
    """

    class Meta:
        unique_together = ('link', 'category',)

    link = models.URLField()
    name = models.CharField(max_length=100)
    nutriscore = models.CharField(max_length=1)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    img = models.URLField()
