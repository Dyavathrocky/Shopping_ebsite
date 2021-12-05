from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name', 'slug', 'Cat_image')
    list_display_links = ('category_name', 'slug')

    
admin.site.register(Category, CategoryAdmin)


"""prepopulated_fields

    category_name = models.CharField(max_length=50 , unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    Cat_image = models.ImageField(upload_to='photo/categorys', blank=True)"""