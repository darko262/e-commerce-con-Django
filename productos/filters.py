import django_filters
from django import forms
from .models import Producto,Category

#class CategoryFilter(django_filters.FilterSet):
    
 #   class Meta:
#        model = Category
 #       fields = {'name': ['exact']}
#

class ProductFilter(django_filters.FilterSet):
    
    class Meta:
        model = Producto
        fields = {'title':['icontains'], 'categories': ['exact']}