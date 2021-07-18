from django import forms
from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User
from products.models import ProductCategory


class UserAdminRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
    }), required=False)

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', 'password1', 'password2', 'image')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
    }))


class AdminProductCategory(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description', ]
