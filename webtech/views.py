from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    data = {
        'title': 'Home Page',
        'bdata': 'Welcome to cubetech',
    }
    return render(request, 'index.html', data)
