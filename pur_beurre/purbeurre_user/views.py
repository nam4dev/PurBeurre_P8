from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import ConnectionForm, AccountForm


def connection(request):
    error = False
    if request.method == "POST":
        form = ConnectionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # Checking identification data
            user = authenticate(username=username, password=password)
            if user:
                # Connecting user
                login(request, user)
            else:
                # prompts an error
                error = True
    else:
        form = ConnectionForm()

    return render(request, 'purbeurre_user/connection.html', locals())


def my_account(request):

    return render(request, 'purbeurre_user/my_account.html', locals())


def disconnection(request):
    logout(request)
    return render(request, 'purbeurre_core/home.html', locals())


def create_account(request):
    error = False

    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            # checking form data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            first_name = form.cleaned_data["first_name"]
            # Creating user
            user = User.objects.create_user(username, username, password)
            user.first_name = first_name
            user.save()
            if user:
                # Connecting user and redirecting to the user's account page.
                login(request, user)
                return redirect('my_account')
            # prompts an error
            else:
                error = True
    else:
        form = AccountForm()

    return render(request, 'purbeurre_user/create_account.html', locals())
