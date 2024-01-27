from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

admin.site.empty_value_display = '-пусто-'


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Админ-зона пользователей Django"""

    list_display = ('id', 'username', 'first_name',
                    'last_name', 'admin_status', 'is_active',)
    search_fields = ('username', 'is_active',)
    list_filter = ('username', 'is_active',)
    list_editable = ('is_active',)

    def admin_status(self, obj):
        return 'Админ' if obj.is_staff else 'Обычный юзер'
    admin_status.short_description = 'Статус пользователя'
