from django.contrib import admin
from HelloProd.infrastructure.models import MyProd

class MyProdModelAdmin(admin.ModelAdmin):
    list_display = ('pid', 'name', 'amount', 'place', 'create_date')

admin.site.register(MyProd, MyProdModelAdmin)