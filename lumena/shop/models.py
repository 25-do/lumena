from django.db import models

# Create your models here.
#
from django.utils.translation import gettext_lazy as _
#
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    class  LabelChoices(models.TextChoices):
        Sale = "SALE", _("Sale")
        New = "New", _("New")
        Promotion  = "Promotion", _("Promotion")

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    label = models.CharField(choices=LabelChoices, max_length=100)


    def __str__(self):
        return self.name


