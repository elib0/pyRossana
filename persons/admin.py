from django.contrib import admin
from persons.models import Promoter, PromoterType, PromoterPhotos


class PromoterAdmin(admin.TabularInline):
    model = PromoterPhotos


admin.site.register(PromoterType)
admin.site.register(Promoter)
