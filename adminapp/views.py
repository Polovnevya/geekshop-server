from django.shortcuts import render

# Create your views here.
from users.models import User


def index(request):
    return render(request, './adminapp/index.html')


def admin_users_read(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, './adminapp/admin-users-read.html',context)


def admin_users_create(request):
    return render(request, './adminapp/admin-users-create.html')


def admin_users_update_delete(request):
    return render(request, './adminapp/admin-users-update-delete.html')
