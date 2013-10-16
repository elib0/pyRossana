from django.db import models
from django.contrib.auth.models import User

MARITAL_STATUS_CHOICES = (
    ('c', 'casado'),
    ('s', 'soltero'),
    ('d', 'divorciado'),
)


class Person(models.Model):
    def __unicode__(self):
        self.user.username

    ci = models.PositiveIntegerField(primary_key=True, max_length=10)
    user = models.OneToOneField(User)
    mobile_phone = models.CharField(max_length=12)
    address = models.TextField()
    day_registration = models.DateTimeField(auto_now=True)


class PromoterType(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=30)
    desciption = models.TextField(max_length=100)


class Promoter(Person):
    def __unicode__(self):
        self.user.name

    age = models.SmallIntegerField(max_length=2)
    marital_status = models.CharField(max_length=1,
                                        choices=MARITAL_STATUS_CHOICES,
                                        default=MARITAL_STATUS_CHOICES[0]
                                    )
    height = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    phone = models.CharField(max_length=12, blank=True, null=True)
    pin = models.CharField(max_length=8, blank=True, null=True)
    desciption = models.TextField(blank=True, null=True)
    rol = models.OneToOneField(PromoterType)
    studying = models.BooleanField()


class PromoterPhoto(models.Model):
    def __unicode__(self):
        self.promoter
    promoter = models.ForeignKey(Promoter)
    # photo = models.ImageField(upload_to="promoter_photos")
