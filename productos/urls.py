from django.urls import path
from . import views

urlpatterns = [
path('', views.productos, name="productos"),
path('<slug:category_slug>/', views.productos, name="productos_category"),
path('<slug:category_slug>/<slug:product_slug>/', views.productos_detail, name="productos_detail"),

]