from django.db import models
from purbeurre_off.models import Product
from purbeurre_user.models import User


# Create your models here.
class FavoriteManager(models.Manager):
    def save(self, product, user):
        self.get_or_create(
            favorite_id=product,
            user_id=user.id
        )

    def remove(self, product, user):
        favorite = self.get(
            favorite_id=product,
            user_id=user.id
        )
        favorite.delete()


class Favorite(models.Model):

    class Meta:
        unique_together = ('user', 'favorite')

    objects = FavoriteManager()

    favorite = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='favorite')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
