from django.shortcuts import render, HttpResponse
from core.models import Bottle
# core/views.py

def contacts(request):
    return render(request, 'core/contacts.html')

def about(request):
    return render(request, 'about.html')

def makers_list(request):
    context = {}
    # SELECT * FROM Botlle
    bottles_list = Bottle.objects.all()
    context["bottles_list"] = bottles_list
    return render(request, 'makers.html', context)
