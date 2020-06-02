from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from purbeurre_off.models import Product

# Create your views here.


# index
def favorites(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    # user = ???
    # favorites = Product.objects.filter(user__iexact=user)
    return render(request, 'purbeurre_favorites/favorites.html', locals())


def save(request):
    # enreg un produit dans la DB
    pass


def delete(request):
    # suppr un prod de la base
    pass
