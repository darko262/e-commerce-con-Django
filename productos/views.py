from django.shortcuts import render, get_object_or_404
from .models import Producto, Category
from .filters import ProductFilter #CategoryFilter
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

# Create your views here.
def productos(request ,category_slug=None):
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
    return render(request, "productos/productos.html ",contex)

def productos_detail(request, category_slug, product_slug):
    try:
        single_product= Producto.objects.get(categories__slug=category_slug, slug2=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    
    contex = { 
        'single_product':single_product,
        'in_cart':in_cart
        }

    return render (request, 'productos/productos_detail.html', contex)

    
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Producto.objects.order_by('-created').filter(Q(content__icontains=keyword) | Q(title__icontains=keyword))
            product_count=products.count()
        else: 
            if keyword == '':
                products = Producto.objects.all().filter(is_avaible=True)
                product_count=products.count()
                
    contex ={
        'productos':products,
        'product_count':product_count,
    }
    return render(request, "productos/productos.html",contex)