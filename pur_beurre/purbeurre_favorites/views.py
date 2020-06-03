from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from purbeurre_off.models import Product
from purbeurre_user.models import User
from purbeurre_favorites.models import Favorite

# Create your views here.


# index
def favorites(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    user = request.user
    favorites = Favorite.objects.filter(user__iexact=user)
    return render(request, 'purbeurre_favorites/favorites.html', locals())


def save(request):
    # enreg un produit dans la DB
    Favorite.objects.get_or_create(
        favorite=request.product,
        user=request.user
    )


def delete(request):
    # suppr un prod de la base
    favorite = Favorite(
        favorite=request.product,
        user=request.user)
    favorite.delete()
