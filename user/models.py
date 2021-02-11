from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, is_active=True, is_staff=False, is_admin=False, is_superuser=False):
        if not username or not password:
            raise ValueError("User must have both username and password")
        user_obj = self.model(
            username = username
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.superuser = is_superuser
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, username, password):
        user = self.create_user(username, password=password,is_staff=True)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password=password,is_staff=True, is_admin=True, is_superuser = True)
        return user

class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.superuser

    @property
    def is_admin(self):
        return self.admin

    objects = UserManager()