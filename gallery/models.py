from django.db import models


class Album(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField('Nombre Carpeta', max_length=20)
    last_modification = models.DateField('Ultima modificación',
                                         auto_now=True,
                                         auto_now_add=True)


class Picture(models.Model):
    def __str__(self):
        return self.title
    folder = models.ForeignKey(Album)
    title = models.CharField('Titulo', max_length=15)
    picture = models.ImageField('Foto')


class Comment(models.Model):
    picture = models.ForeignKey(Picture)
    text = models.TextField("comentario")
    date = models.DateField("Fecha de publicación")
