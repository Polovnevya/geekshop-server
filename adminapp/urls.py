"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from .views import index, admin_users_read, admin_users_create, admin_users_update_delete

app_name = 'adminapp'
urlpatterns = [
    path('', index, name='index'),
    path('users', admin_users_read, name='admin_users_read'),
    path('users_create', admin_users_create, name='admin_users_create'),
    path('users_update_delete', admin_users_update_delete, name='admin_users_update_delete'),

]
