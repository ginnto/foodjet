from django.contrib import admin
from . models import *
# Register your models here.

# class cartadmin(admin.ModelAdmin):

admin.site.register(cartlist)
admin.site.register(items)


