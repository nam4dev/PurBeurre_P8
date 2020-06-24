from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from purbeurre_off.models import Product
from purbeurre_user.models import User
from purbeurre_favorites.models import Favorite
from django.forms.models import model_to_dict

# Create your views here.


# index
def favorites(request):
    """ Shows the favorites saved by the user. """
    user = request.user
    favorites_found = Favorite.objects.filter(user__exact=user)
    favorites_saved = []
    for product in favorites_found:
        favorite_prod = Product.objects.search_favorite(product.favorite_id)
        favorites_saved.append(favorite_prod)
    return render(request, 'purbeurre_favorites/favorites.html', locals())


def save(request):
    """ Saves a new product for the user in the favorites table of the DB"""
    product = request.GET.get('product')
    user = request.user
    Favorite.objects.save(product, user)
    return redirect('favorites')


def remove(request):
    """ Removes a new product for the user in the favorites table of the DB"""
    product = request.POST.get('product')
    user = request.user
    Favorite.objects.remove(product, user)
    return redirect('favorites')
