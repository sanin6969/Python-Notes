from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator

class Color(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True)  # Optional image field
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    class Meta:
        unique_together = (('product', 'color', 'size'),)
