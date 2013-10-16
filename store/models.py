from django.db import models


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
    # photo = models.ImageField(upload_to="promoter_photos")
