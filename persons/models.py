from django.db import models
from django.contrib.auth.models import User

MARITAL_STATUS_CHOICES = (
    ('c', 'casado'),
    ('s', 'soltero'),
    ('d', 'divorciado'),
)

SCHEDULE_CHOICES = (
    (1, 'Manana'),
    (2, 'Tarde'),
    (3, 'Noche'),
)

User.add_to_class('ci', models.PositiveIntegerField(unique=True,
                                                    default=0,
                                                    max_length=10))
User.add_to_class('mobile_phone', models.CharField(max_length=12))
User.add_to_class('address', models.TextField())


class PromoterType(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)
    desciption = models.TextField(max_length=100, null=True)


class Promoter(models.Model):
    def __str__(self):
        self.user.name

    user = models.OneToOneField(User)
    age = models.DateField()
    marital_status = models.CharField(max_length=1,
                                      choices=MARITAL_STATUS_CHOICES,
                                      default=MARITAL_STATUS_CHOICES[0])
    height = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    phone = models.CharField(max_length=12, blank=True, null=True)
    pin = models.CharField(max_length=8, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rol = models.OneToOneField(PromoterType)
    studying = models.BooleanField()
    study_schedule = models.SmallIntegerField(max_length=1, choices=SCHEDULE_CHOICES)


class PromoterPhotos(models.Model):
    def __str__(self):
        self.promoter.user.username

    promoter = models.OneToOneField(Promoter)
    photo1 = models.ImageField(upload_to="promoter_photos")
    photo2 = models.ImageField(upload_to="promoter_photos")
