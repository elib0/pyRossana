from django.contrib import admin
from persons.models import Promoter, PromoterType, PromoterPhotos


class PhotosInline(admin.TabularInline):
    model = PromoterPhotos
    extra = 1


class PromoterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile_phone', 'status')
    inlines = [PhotosInline]


admin.site.register(PromoterType)
admin.site.register(Promoter, PromoterAdmin)
