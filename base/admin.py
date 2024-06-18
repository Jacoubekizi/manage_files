from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .froms import *
# Register your models here.

class UserAdmin(UserAdmin):


    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ['username','id', 'user_type', 'first_name', 'last_name', 'is_staff']
    fieldsets = (
    (None, 
         {'fields':('username','password',)}
     ),
    ('User Information',
        {'fields':('first_name', 'last_name')}
    ),
    ('Permissions', 
        {'fields':('user_type', 'is_staff', 'is_superuser', 'is_active', 'groups','user_permissions')}
    ),
    ('Registration', 
        {'fields':('date_joined', 'last_login',)}
    )
    )
    add_fieldsets = (
        (None, {'classes':('wide',),
            'fields':(
                'username','user_type', 'password1', 'password2',
            )}
            ),
        )
    search_fields = ('username',"user_type",)
    ordering = ("user_type",)

admin.site.register(User, UserAdmin)


class AdminUplodFile(admin.ModelAdmin):
    list_display = ['id', 'user', 'file', 'note', 'type_file','created_at']

class AdminStatusFile(admin.ModelAdmin):
    list_display = ['id', 'file', 'status', 'note', 'created_at']

admin.site.register(UploadFile, AdminUplodFile)
admin.site.register(StatusFile, AdminStatusFile)

admin.site.register(OrderFile)