from django.contrib import admin
from .models import Producto,Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductosAdmin(admin.ModelAdmin):
    list_display=('title','price','stock','updated','is_avaible','categories')
    prepopulated_fields={'slug2':('title',)}
    readonly_fields = ('created', 'updated')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Producto, ProductosAdmin)

