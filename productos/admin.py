from django.contrib import admin
from .models import Producto,Category,Variation

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductosAdmin(admin.ModelAdmin):
    list_display=('title','price','stock','updated','is_avaible','categories')
    prepopulated_fields={'slug2':('title',)}
    readonly_fields = ('created', 'updated')

class VarationsAdmin(admin.ModelAdmin):
    list_display=('product','variation_category','variation_value','is_active')
    list_editable =('is_active',)
    list_filter = ('product','variation_category','variation_value','is_active')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Variation,VarationsAdmin)

