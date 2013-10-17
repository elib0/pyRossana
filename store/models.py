from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('', 'elito'),
)


class Categorie(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()


class SubCategorie(models.Model):
    categorie = models.ForeignKey(Categorie)
    name = models.CharField(max_length=45)
    details = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    details = models.TextField()
    sub_categorie = models.ForeignKey(SubCategorie)


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product)
    # photo = models.ImageField(upload_to="product_photos")


class Cart(models.Model):
    user = models.ForeignKey(User)
    creation_date = models.DateField(auto_now_add=True)
    purchase_date = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


class ProductsCart(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
