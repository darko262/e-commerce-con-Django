from django.shortcuts import render, HttpResponse, get_object_or_404
from productos.models import Producto,Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

def principal(request ,category_slug=None):
    categories2= None
    productos= None
    if category_slug != None:
        categories2= get_object_or_404(Category, slug=category_slug)
        productos= Producto.objects.filter(categories=categories2 ,is_avaible=True)
        paginator = Paginator(productos, 4)
        page= request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count=productos.count()
    else:
        productos = Producto.objects.all().filter(is_avaible=True)
        paginator = Paginator(productos, 4)
        page= request.GET.get('page')
        paged_product = paginator.get_page(page)

        #filtro= ProductFilter(request.GET, queryset=Producto.objects.all())
        product_count=productos.count()
    #fcategor= CategoryFilter(request.GET, queryset=Category.objects.all())#fcategor': fcategor        productos= Producto.objects.filter(categorys=categories2 ,is_avaible=True)
        #product_count=productos.count()
    
    contex={
        'productos':paged_product,#'filtrado' : filtro 
        'product_count':product_count,
    }
    return render(request, 'core/principal.html',contex)


# Create your views here.

def about(request):
    return render(request, "core/about.html")
