#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

MARITAL_STATUS_CHOICES = (
    ('c', 'Casado'),
    ('s', 'Soltero'),
    ('d', 'Divorciado'),
)

SCHEDULE_CHOICES = (
    (1, 'Mañana'),
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

    name = models.CharField('Nombre', max_length=30)
    desciption = models.TextField('Descripción', max_length=100, null=True,)


class Promoter(models.Model):
    def __str__(self):
        self.user.name

    ci = models.PositiveIntegerField('Cedula',
                                     unique=True,
                                     default=0,
                                     max_length=10)
    first_name = models.CharField('Nombre', max_length=30)
    last_name = models.CharField('Apellido', max_length=30)
    age = models.DateField('Fecha Nacimiento')
    marital_status = models.CharField('Estado Civil', max_length=1,
                                      choices=MARITAL_STATUS_CHOICES,
                                      default=MARITAL_STATUS_CHOICES[0])
    height = models.DecimalField('Estatura', max_digits=4, decimal_places=2)
    weight = models.DecimalField('Peso(KG)', max_digits=4, decimal_places=2)
    measure = models.CommaSeparatedIntegerField(max_length=8)
    mobile_phone = models.CharField('Teléfono móvil', max_length=12)
    phone = models.CharField('Teléfono habitación', max_length=12, blank=True, null=True)
    pin = models.CharField('Blackberry PIN', max_length=8, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rol = models.ManyToManyField(PromoterType, verbose_name=u'Tipo de promotor')
    studying = models.BooleanField('¿Estudias?')
    study_schedule = models.SmallIntegerField('Turno de estudio',
                                              max_length=1,
                                              choices=SCHEDULE_CHOICES)


class PromoterPhotos(models.Model):
    def __str__(self):
        self.promoter.user.username

    promoter = models.OneToOneField(Promoter)
    photo1 = models.ImageField(upload_to="promoter_photos")
    photo2 = models.ImageField(upload_to="promoter_photos")
