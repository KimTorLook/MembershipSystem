from django.contrib import admin
from myapp.models import Craftsman

#admin.site.register(Craftsman)

class CraftsmanAdmin(admin.ModelAdmin):
    list_display=('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')
    list_filter=('cName','cSex')
    search_fields=('cName',)
    ordering=('id',)

admin.site.register(Craftsman,CraftsmanAdmin)