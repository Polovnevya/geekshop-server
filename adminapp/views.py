from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from users.models import User
from products.models import ProductCategory
from adminapp.forms import UserAdminRegistrationForm, UserAdminProfileForm, AdminProductCategory


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
        form = UserAdminRegistrationForm()

    context = {
        'title': 'Админ панель -  создание пользователя',
        'form': form
    }
    return render(request, './adminapp/admin-users-create.html', context)


def admin_users_delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return HttpResponseRedirect(reverse('adminapp:admin_users_read'))


def admin_users_update(request, id):
    selected_user = User.objects.get(pk=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users_read'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {
        'title': 'Админ панель -  редактирование пользователя',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, './adminapp/admin-users-update-delete.html', context)


######################################################################
def admin_category_read(request):
    context = {
        'title': 'Админ панель - категории',
        'categories': ProductCategory.objects.all()
    }
    return render(request, './adminapp/admin-category-read.html', context)


def admin_category_create(request):
    if request.method == 'POST':
        form = AdminProductCategory(files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_category_read'))
    else:
        form = AdminProductCategory()

    context = {
        'title': 'Админ панель -  создание категории',
        'form': form
    }
    return render(request, './adminapp/admin-category-create.html', context)
