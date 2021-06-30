from django.db import models
from django.utils import timezone


# Create your models here.


class AbstractBaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, default=None)
    deleted_at = models.DateTimeField(
        null=True, default=None
    )

    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        abstract = True
        ordering = [
            "created_at",
        ]


class Product(AbstractBaseModel):
    name = models.CharField(max_length=350)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images', blank=True)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
