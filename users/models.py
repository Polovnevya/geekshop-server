from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()
