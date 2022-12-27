from django.shortcuts import render, get_object_or_404
from .models import Producto, Category
from .filters import ProductFilter #CategoryFilter

# Create your views here.
def productos(request ,category_slug=None):
    categories2= None
    productos= None
    if category_slug != None:
        categories2= get_object_or_404(Category, slug=category_slug)
        productos= Producto.objects.filter(categories=categories2 ,is_avaible=True)
        product_count=productos.count()
    else:
        productos = Producto.objects.all().filter(is_avaible=True)
        #filtro= ProductFilter(request.GET, queryset=Producto.objects.all())
        product_count=productos.count()
    #fcategor= CategoryFilter(request.GET, queryset=Category.objects.all())#fcategor': fcategor        productos= Producto.objects.filter(categorys=categories2 ,is_avaible=True)
        #product_count=productos.count()
    
    contex={
        'productos':productos,#'filtrado' : filtro 
        'product_count':product_count,
    }
    return render(request, "productos/productos.html",contex)

def productos_detail(request, category_slug, product_slug):
    try:
        single_product= Producto.objects.get(categories__slug=category_slug, slug2=product_slug)
    except Exception as e:
        raise e
    
    contex = { 
        'single_product':single_product,
        }

    return render (request, 'productos/productos_detail.html', contex)