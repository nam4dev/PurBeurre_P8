from django.db import models
from purbeurre_off.models import Product
from purbeurre_user.models import User


# Create your models here.
class Favorite(models.Model):
    favorite: models.ForeignKey = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='favorite')
    user: models.ForeignKey = models.ForeignKey(
        User, on_delete=models.CASCADE)
    objects: models.Manager = models.Manager()


class Meta:
    unique_together = ('user', 'favorite')
