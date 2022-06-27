from django.contrib import admin
from . models import *

# Register your models here.

class  catadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(categ,catadmin)

class product(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','img','available']
    list_editable=['price','stock','img','available']       # evide name kodukkan pattilla error akum bcz slug is there
    prepopulated_fields ={'slug':('name',)}
admin.site.register(products,product)

