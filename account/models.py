from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), max_length=100, unique=True, db_index=True)
    username = models.CharField(_('username'), max_length=50, unique=True, db_index=True)
    first_name = models.CharField(_("user's first name"), max_length=50, blank=True, null=True)
    last_name = models.CharField(_("user's last name"), max_length=50, blank=True, null=True)
    number = models.CharField(_("user's mobile number"), max_length=10, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 

    class Meta:
        verbose_name='user'
        verbose_name_plural='users'

    def __str__(self):
        return self.username
