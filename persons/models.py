from django.db import models
from django.contrib.auth.models import User


CIVIL_STATUS_CHOICES = (
    ('c', _('casado')),
    ('s', _('soltero')),
    ('d', _('divorciado')),
)


class Person(models.Model):
    ci = models.PositiveIntegerField(primary_key=True, max_lenght=10)
    user = models.OneToOneField(User)
    mobile_phone = models.CharField(max_length=12)
    address = models.TextField()
    day_registration = models.DateTimeField(auto_now=True)


class PromoterType(models.Model):
    name = models.CharField(max_length=30)
    desciption = models.TextField(max_length=100)


class Promoter(Person):
    age = models.SmallIntegerField(max_length=2)
    marital_status = models.CharField(max_length=1,
                                        choices=CIVIL_STATUS_CHOICES,
                                        default=CIVIL_STATUS_CHOICES[0]
                                    )
    height = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    phone = models.CharField(max_length=12)
    pin = models.CharField(max_length=8)
    desciption = models.TextField()
    rol = models.OneToOneField(PromoterType)


class PromoterPhoto(models.Model):
    promoter = models.ForeignKey(Promoter)
    photo = models.ImageField()
