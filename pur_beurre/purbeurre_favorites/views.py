from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.


# index
def favorites(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return render(request, 'purbeurre_favorites/favorites.html')