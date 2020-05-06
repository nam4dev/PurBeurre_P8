from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from .forms import ConnectionForm


# Create your views here.

def connection(request):
    error = False

    if request.method == "POST":
        form = ConnectionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnectionForm()

    return render(request, 'purbeurre_user/connection.html', locals())


def my_account(request):

    return render(request, 'purbeurre_user/my_account.html', locals())


def disconnection(request):
    logout(request)
    return redirect(reverse(connection))