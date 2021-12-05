from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import fields
from .models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email','username', 'first_name','last_login', 'date_joined', 'last_name',  'is_staff', 'is_active')
    list_display_links = ('email','username', 'first_name')
    readonly_fields = ('last_login', 'date_joined')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('-date_joined',)



admin.site.register(Account, AccountAdmin)


"""    first_name = models.CharField(max_length=50)
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
    is_superadmin = models.BooleanField(default=False)"""