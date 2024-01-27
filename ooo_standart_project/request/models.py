from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from api.constants import (STATUS_CHOICES, PAYMENT_CHOICES,
                           ACCOUNT_TYPE, REQUISITE_MAX_LENGTH)


class Requisite(models.Model):
    """ Модель реквизитов. """

    payment_type = models.CharField(
        'Тип платежа', choices=PAYMENT_CHOICES,
        max_length=REQUISITE_MAX_LENGTH)

    account_type = models.CharField(
        'Тип карты/счёта', choices=ACCOUNT_TYPE,
        max_length=REQUISITE_MAX_LENGTH)

    first_name = models.CharField('Имя', max_length=REQUISITE_MAX_LENGTH)
    last_name = models.CharField('Фамилия', max_length=REQUISITE_MAX_LENGTH)
    middle_name = models.CharField(
        'Отчество', max_length=REQUISITE_MAX_LENGTH, blank=True)
    phone_number = PhoneNumberField()
    card_limit = models.DecimalField(
        'Лимит доступных средств', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизиты'

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name}, тел.: {self.phone_number}'


class PaymentRequest(models.Model):
    """ Модель заявки на оплату. """

    amount = models.DecimalField(
        'Сумма оплаты', max_digits=10, decimal_places=2)
    requisites = models.ForeignKey(
        Requisite,
        on_delete=models.PROTECT,
        verbose_name='Реквизиты заявки')

    status = models.CharField(
        'Статус заявки', choices=STATUS_CHOICES,
        max_length=REQUISITE_MAX_LENGTH)

    created = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('-created',)

    def __str__(self) -> str:
        return f'{self.requisites} {self.status}'
