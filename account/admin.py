from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from account.models import CustomUser

USERNAME_FIELD = get_user_model().USERNAME_FIELD
REQUIRED_FIELDS = (USERNAME_FIELD,) + tuple(get_user_model().REQUIRED_FIELDS)

BASE_FIELDS = (
    "Base Fields",
    {
        'fields' : REQUIRED_FIELDS + ('password',)
    }
)

SIMPLE_PERMISSION_FIELDS = (
    _('Permissions'), 
    {
        'fields': ('is_active', 'is_superuser', 'is_staff')
    }
)

ADVANCE_PERMISSION_FIELDS = (
    _('Advance Fields'),
    {
        'fields': ('groups', 'user_permissions')
    }
)

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')
    readonly_fields = ('last_login',)
    fieldsets = (
        BASE_FIELDS,
        (_('Optional Fields'), {'fields' : ('first_name', 'last_name', 'number')}),
        SIMPLE_PERMISSION_FIELDS,
        ADVANCE_PERMISSION_FIELDS,
        (_("Important Dates"), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {'fields': REQUIRED_FIELDS + ('password1', 'password',)},)
    ,)
admin.site.register(CustomUser, CustomUserAdmin)
