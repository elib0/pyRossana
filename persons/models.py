#encoding:utf-8
from django.db import models

MARITAL_STATUS_CHOICES = (
    ('n', 'Seleccione su estado civil'),
    ('c', 'Casado'),
    ('s', 'Soltero'),
    ('d', 'Divorciado'),
)

SCHEDULE_CHOICES = (
    (0, 'Elija su turno de estudio'),
    (1, 'Mañana'),
    (2, 'Tarde'),
    (3, 'Noche'),
)

NUMBER_CHOICE = (
    ('-1', '¿Tienes Hijos?'),
    (1, '0'),
    (1, '1'),
    (2, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
)

STATUS_CHOICES = (
    (0, 'Pendiente'),
    (1, 'Revisado'),
    (2, 'Rechazado'),
    (3, 'Aceptado'),
)


class PromoterType(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField('Nombre', max_length=30)
    desciption = models.TextField('Descripción', max_length=100, null=True,)


class Promoter(models.Model):
    def __str__(self):
        return self.first_name

    ci = models.PositiveIntegerField('Cedula',
                                     unique=True,
                                     max_length=10)
    first_name = models.CharField('Nombre', max_length=30)
    last_name = models.CharField('Apellido', max_length=30)
    age = models.DateField('Fecha Nacimiento')
    mobile_phone = models.CharField(u'Teléfono móvil', max_length=12)
    phone = models.CharField(u'Teléfono habitación', max_length=12, blank=True, null=True)
    address = models.TextField(u'Dirección')
    marital_status = models.CharField('Estado Civil', max_length=1,
                                      choices=MARITAL_STATUS_CHOICES,
                                      default=MARITAL_STATUS_CHOICES[0])
    height = models.DecimalField('Estatura', max_digits=4, decimal_places=2)
    weight = models.DecimalField('Peso(KG)', max_digits=4, decimal_places=2)
    pin = models.CharField('Blackberry PIN', max_length=8, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rol = models.ManyToManyField(PromoterType, verbose_name=u'Tipo de promotor')
    num_children = models.SmallIntegerField('Numero de Hijos',
                                            choices=NUMBER_CHOICE,
                                            default=NUMBER_CHOICE[0])
    studying = models.BooleanField(u'¿Estudias?', blank=True, default=False)
    study_schedule = models.SmallIntegerField('Turno de estudio',
                                              max_length=1,
                                              choices=SCHEDULE_CHOICES,
                                              default=SCHEDULE_CHOICES[0],)
    measure1 = models.IntegerField()
    measure2 = models.IntegerField()
    measure3 = models.IntegerField()
    photo1 = models.ImageField(upload_to="promoter_photos")
    photo2 = models.ImageField(upload_to="promoter_photos")
    status = models.IntegerField(max_length=1,
                                 choices=STATUS_CHOICES,
                                 default=STATUS_CHOICES[0],)
