from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ("username","is_admin","date_moved_to_germany","years_in_germany")
    list_filter = ("is_admin","is_staff","groups")
    fieldsets = (
        (None,{"fields":("username","password")}),
        ("Personal info",{"fields":("date_moved_to_germany","years_in_germany")}),
        ("Permissions",{"fields":("is_admin","is_staff","groups")})
    )
    ordering = ("id",)
    search_fields = ("username",)
    filter_horizontal = ("groups",)
 
admin.site.register(CustomUser,UserAdmin)