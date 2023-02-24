from django.contrib import admin
from .models import Account
from django.contrib.auth.models import User
# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display=('email','first_name','last_name','username','last_login','date_joined','is_active')

class UserAdmin(admin.ModelAdmin):
    list_display=('username','last_name','email','last_login','date_joined','is_active','is_staff')
    



# Register your models here.
admin.site.register(Account, AccountAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

