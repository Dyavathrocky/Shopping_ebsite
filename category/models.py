from enum import unique
from django.db import models
from django.db.models.base import Model

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50 , unique=True)
    slug = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    Cat_image = models.ImageField(upload_to='photo/categorys', blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.categry_name
