from django.contrib import admin

from .models import Requisite, PaymentRequest

admin.site.empty_value_display = '-пусто-'


@admin.register(Requisite)
class RequisiteAdmin(admin.ModelAdmin):
    list_display = ('payment_type', 'account_type', 'first_name',
                    'last_name', 'middle_name', 'phone_number', 'card_limit')
    search_fields = ('payment_type', 'account_type', 'first_name',
                     'last_name', 'middle_name', 'phone_number', 'card_limit')
    list_filter = ('payment_type', 'account_type', 'first_name',
                   'last_name', 'middle_name', 'phone_number', 'card_limit')


@admin.register(PaymentRequest)
class PaymentRequestAdmin(admin.ModelAdmin):
    list_display = ('amount', 'requisites', 'status', 'created')
    search_fields = ('amount', 'requisites', 'status', 'created')
    list_filter = ('amount', 'requisites', 'status', 'created')

    def new_format_created(self, obj):
        return obj.date.strftime('%d.%b.%Y')
    new_format_created.short_description = 'Дата создания заявки'
