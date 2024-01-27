STATUS_CHOICES = [
    ('Awaiting', 'Ожидает оплаты'),
    ('Paid', 'Оплачена'),
    ('Cancelled', 'Отменена'),
]

PAYMENT_CHOICES = [
    ('Card', 'Карта'),
    ('Payment account', 'Платежный счет'),
]

REQUISITE_MAX_LENGTH = 100

ACCOUNT_TYPE = [
    ('Debit card', 'Дебетовая карта'),
    ('Credit card', 'Кредитная карта'),
    ('Organization account', 'Счёт огранизации'),
    ('Individual account', 'Счёт физического лица'),
]


USER = 'user'
ADMIN = 'admin'

USER_ROLES = [
    (USER, 'user'),
    (ADMIN, 'admin'),
]

MAX_USER_MODEL_FIELD_LENGTH = 150

REQUIRED_FIELDS = ['password', 'first_name', 'last_name', ]

PAGINATION_PAGE_SIZE = 10
