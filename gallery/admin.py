from django.contrib import admin
from gallery.models import Album, Picture


class PicturesInline(admin.TabularInline):
    model = Picture
    extra = 4


class AlbumAdmin(admin.ModelAdmin):
    inlines = [PicturesInline]


admin.site.register(Album, AlbumAdmin)
