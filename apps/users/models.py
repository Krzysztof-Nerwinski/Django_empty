from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _

from apps.users.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name=_('Adres email'), max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name')

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('użytkownik')
        verbose_name_plural = _('użytkownicy')

    def __str__(self):
        return self.email
