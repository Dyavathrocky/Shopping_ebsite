from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','category', 'price', 'stock','is_avilable','modified_date')
    prepopulated_fields = {'slug':('product_name',)}
    #list_display_links = ('product_name', 'category')


admin.site.register(Product, ProductAdmin)




"""    product_name = models.CharField(max_length=200, unique=True)
    slug         = models.SlugField(max_length=200, unique=True)
    description  = models.TextField()
    price        = models.IntegerField()
    image        = models.ImageField(upload_to = 'photo/prducts')
    stock        = models.IntegerField()
    is_avilbale  = models.BooleanField(default=True)
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now = True)"""
