from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, date_moved_to_germany=None, 
                    years_in_germany=None, is_active=True, is_staff=False, is_admin=False):
        if not username or not password:
            raise ValueError("User must have both username and password")
        user_obj = self.model(
            username = username
        )
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.years_in_germany = years_in_germany
        user_obj.date_moved_to_germany = date_moved_to_germany
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, username, password,**other_fields):
        user = self.create_user(username, 
                                password=password,
                                is_staff=True)
        return user

    def create_superuser(self, username, password,**other_fields):
        user = self.create_user(username, 
                                password=password,
                                is_staff=True,
                                is_admin=True)
        return user

class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_moved_to_germany = models.DateField(blank=True,null=True)
    years_in_germany = models.IntegerField(blank=True, null=True,default=0)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    