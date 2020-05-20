from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from purbeurre_off.models import Product

# Create your views here.


# index
def favorites(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    # favorites = Product.objects.filter(user__iexact=user)
    return render(request, 'purbeurre_favorites/favorites.html', locals())