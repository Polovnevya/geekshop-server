from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from users.models import User
from adminapp.forms import UserAdminRegistrationForm


def index(request):
    context = {
        'title': 'Админ панель',
    }
    return render(request, './adminapp/index.html', context)


def admin_users_read(request):
    context = {
        'title': 'Админ панель - пользователи',
        'users': User.objects.all()
    }
    return render(request, './adminapp/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users_read'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegistrationForm()

    context = {
        'title': 'Админ панель -  создание пользователя',
        'form': form
    }
    return render(request, './adminapp/admin-users-create.html', context)


def admin_users_delete(request, id):
    pass


def admin_users_update(request, id):
    context = {
        'title': 'Админ панель -  изменение и удаление пользователя',
    }
    return render(request, './adminapp/admin-users-update-delete.html', context)
