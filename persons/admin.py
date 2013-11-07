from django.contrib import admin
from persons.models import Promoter, PromoterType


class PromoterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile_phone', 'status')


admin.site.register(PromoterType)
admin.site.register(Promoter, PromoterAdmin)
