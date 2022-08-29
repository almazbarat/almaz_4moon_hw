"""water URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clients.views import *
from core.views import contacts, about, makers_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts),
    path('about/', about),
    path('makers/', makers_list),
    path('clients/', client_list, name="client-list"),
    path('orders/', order_list, name="orders-list"),
    path('client/<int:id>/', client_detail, name="client-detail"),
    path('order/<int:id>/', order_detail, name="order-detail"),
    path('client/update/<int:id>/', client_update, name="client-update"),
    path('order/update/<int:id>/', order_update, name="order-update"),
    path('order/create/', create_order, name="create-order"),
    path('order/djangoform/', order_djangoform, name="order-djangoform"),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)