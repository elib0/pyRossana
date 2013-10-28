from django.contrib import admin
from store.models import Categorie, Product, ProductPhoto


class PhotosInline(admin.TabularInline):
    model = ProductPhoto
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotosInline]

admin.site.register(Categorie)
admin.site.register(Product, ProductAdmin)
