from django.shortcuts import render, HttpResponse
from .models import Client, Order
from .forms import OrderForm, ClientForm, UpOrderForm

def client_list(request):
    context ={}
    context["clients"] = Client.objects.all()
    return render(request, 'clients.html', context)

def client_detail(request, id):
    context = {
        "client" : Client.objects.get(id=id)
    } #SELECT * FROM Client WHERE id=id
    return render(request, "client_info.html", context)


def client_update(request, id):
    context = {}
    client_object = Client.objects.get(id=id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client_object)
        if form.is_valid():
            client_object = form.save()
    context["form"] = ClientForm(instance=client_object)
    return render(request, 'client_update.html', context)


def create_order(request):
    if request.method == "POST":
        data = request.POST
        order = Order()
        order.name = data['name']
        order.contacts = data['contacts']
        order.description = data['description']
        order.save()
        # INSERT INTO order
        return HttpResponse("Форма обработана")
    return render(request, 'core/order_form.html')


def order_djangoform(request):
    context = {}
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return HttpResponse("Форма обработана")
        return HttpResponse("Данные не Валидны")
    
    context["order_form"] = OrderForm()
    return render(request, 'order_djangoform.html', context)



def order_list(request):
    context ={}
    context["orders"] = Order.objects.all()
    return render(request, 'orders.html', context)


def order_detail(request, id):
    context = {
        "order" : Order.objects.get(id=id)
    } #SELECT * FROM Client WHERE id=id
    return render(request, "order_info.html", context)

def order_update(request, id):
    context = {}
    order_object = Order.objects.get(id=id)
    if request.method == "POST":
        up_order_form = UpOrderForm(request.POST, instance=order_object)
        if up_order_form.is_valid():
            order_object = up_order_form.save()
    context["up_order_form"] = UpOrderForm(instance=order_object)
    return render(request, 'order_update.html', context)


def order_del(request, id):
    context = {}
    order_object = Order.objects.get(id=id)
    if request.method == "POST":
        del_order_form = UpOrderForm(request.POST, instance=order_object)
        order_object.delete()
        order_object = del_order_form.save()
    context["del_order_form"] = UpOrderForm(instance=order_object)
    return render(request, 'order_update.html', context)
    


