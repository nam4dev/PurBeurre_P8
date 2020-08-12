from django.shortcuts import render


# home
def home(request):
    return render(request, 'purbeurre_core/home.html')


# legal notices
def legal_notices(request):
    return render(request, 'purbeurre_core/legal_notices.html')
