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
from core.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import View, TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', makers_list),
    path('contacts/', contacts),
    path('about/', about, name="about"),
    path('signin/', LoginView.as_view(), name="sign-in"), 
    path("exit/", logout, name="logout"),
    
    path('clients/', ClientListView.as_view(), name="client-list"),
    path('client/update/<int:id>/', client_update, name="client-update"),
    path('client/<int:pk>/', ClientDetailView.as_view(), name="client-detail"),
    path('client/<int:id>/order-list', ClientOrderList.as_view(), name="client-order-list"),
    
    # path('orders/', OrderListView.as_view(), name="orders-list"),
    path('orders/', order_list, name="orders-list"),
    path('order/<int:pk>/', OrderDetailView.as_view(), name="order-detail"),
    path('order/update/<int:id>/', order_update, name="order-update"),
    path('order/create/', create_order, name="create-order"),
    path('order/djangoform/', order_djangoform, name="order-djangoform"),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)