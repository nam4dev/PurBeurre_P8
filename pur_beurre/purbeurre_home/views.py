from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.


# index
def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return render(request, 'purbeurre_home/home.html')

# # exemples
# # page not found
# def fonction_appelee(request, erreur):
#     # Si erreur, afficher page not found (404)
#     if erreur:
#         raise Http404
#
#     return HttpResponse('le retour normal sans erreur')
#
# # redirection
# # cf cours
# # https://openclassrooms.com/fr/courses/1871271-developpez-votre-site-web-avec-le-framework-django/1871890-votre-premiere-page-grace-aux-vues
# def fonction_appelee(request, args):
#     return redirect("url vers laquelle on redirige/ ")