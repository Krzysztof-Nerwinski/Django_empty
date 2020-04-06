from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import CustomUser
from django.utils.translation import ugettext as _
from django.db.models import Case, When, Value

def change_is_active_status(modeladmin, request, queryset):
    queryset.update(is_active=Case(
        When(is_active=True, then=Value(False)),
        When(is_active=False, then=Value(True))
    ))


def change_is_staff_status(modeladmin, request, queryset):
    queryset.update(is_staff=Case(
        When(is_staff=True, then=Value(False)),
        When(is_staff=False, then=Value(True))
    ))


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # list view
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active')

    # add view
    add_fieldsets = (
        (_('Informacje o użytkowniku'), {'fields': ('first_name', 'last_name', 'email', 'password1', 'password2')}),
        (_('Uprawnienia'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    # change view
    fieldsets = (
        (_('Informacje osobiste'), {'fields': ('email', 'password', 'first_name', 'last_name')}),
        (_('Uprawnienia'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
