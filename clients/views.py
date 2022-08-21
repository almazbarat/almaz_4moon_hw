from django.shortcuts import render
from .models import Client
# Create your views here.
def client_list(request):
    context ={}
    context["clients"] = Client.objects.all()
    return render(request, 'clients.html', context)
