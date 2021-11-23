from enum import unique
from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser

# Create your models here.

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)

    #required

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','lsat_name']


    def __str__(self):
        return self.email

    def has_perm(self, perm , object=None):
        return self.is_admin

    def has_module_perm(self, add_label):
        return True
    



