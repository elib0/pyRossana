#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('p', 'Pendiente'),
    ('c', 'Cancelada'),
    ('o', 'Concretada'),
)


class Categorie(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField('Nombre', max_length=45)
    description = models.TextField('Descripción', null=True)


class SubCategorie(models.Model):
    def __str__(self):
        return self.name
    categorie = models.ForeignKey(Categorie, verbose_name=u'Categoria')
    name = models.CharField('Nombre', max_length=45)
    details = models.TextField('Detalles', null=True)


class Product(models.Model):
    def __str__(self):
        return self.name
    categorie = models.ForeignKey(Categorie, verbose_name=u'Categoría')
    name = models.CharField('Nombre', max_length=45)
    price = models.DecimalField('Precio (BS)', max_digits=8, decimal_places=2)
    details = models.TextField('Detalles')


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product)
    photo = models.ImageField(upload_to="product_photos")


class Cart(models.Model):
    user = models.ForeignKey(User)
    creation_date = models.DateField(auto_now_add=True)
    purchase_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=1,
                              default=STATUS_CHOICES[0],
                              choices=STATUS_CHOICES)


class ProductsInCart(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(max_length=3, default=1)
