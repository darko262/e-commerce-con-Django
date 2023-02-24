from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100, verbose_name="Nombre")
    slug=models.CharField(max_length=100, unique=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def get_url(self):
        return reverse('productos_category', args=[self.slug])

    def __str__(self):
        return self.category_name  
# Create your models here.
class Producto(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre producto", unique=True)
    slug2 = models.CharField(max_length=200, unique=True, null=True)
    content = models.TextField(verbose_name="Descripcion")
    price= models.IntegerField(null=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="productos", null=True)
    stock=models.IntegerField( null=True)
    is_avaible = models.BooleanField(default=True)
    categories=models.ForeignKey(Category, verbose_name="Categorias",on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ['-created']

    def get_url(self):
        return reverse ('productos_detail', args=[self.categories.slug, self.slug2])

    def __str__(self):
        return self.title


class VarationManager(models.Manager):
    def colors(self):
        return super(VarationManager,self).filter(variation_category='color',is_active=True)
    def tallas(self):
        return super(VarationManager,self).filter(variation_category='talla',is_active=True)
    def kilors(self):
        return super(VarationManager,self).filter(variation_category='kilos',is_active=True)
        


variation_category_choise = (
    ('color','color'),
    ('talla','talla'),
    ('kilos','kilos'),
)

class Variation(models.Model):
    product=models.ForeignKey(Producto,on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choise )
    variation_value= models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    objects = VarationManager()

    def __str__(self):
        return self.variation_category + ':' + self.variation_value


  