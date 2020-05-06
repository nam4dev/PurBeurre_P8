from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import ConnectionForm, AccountForm


# Create your views here.

def connection(request):
    error = False

    if request.method == "POST":
        form = ConnectionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            login(request, user)  # nous connectons l'utilisateur
    else:
        form = ConnectionForm()

    return render(request, 'purbeurre_user/connection.html', locals())


def my_account(request):

    return render(request, 'purbeurre_user/my_account.html', locals())


def disconnection(request):
    logout(request)
    return request(request, 'purbeurre_home/home.html')


def create_account(request):
    error = False

    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            first_name = form.cleaned_data["first_name"]
            user = User.objects.create_user(username, username, password)  # Création utilisateur
            user.first_name = first_name
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = AccountForm()

    return render(request, 'purbeurre_user/create_account.html', locals())
