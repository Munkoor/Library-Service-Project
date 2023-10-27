from django.contrib import admin

from library_app.models import (
    Book,
    Borrowing,
    Payment,
)

admin.register(Book)
admin.register(Borrowing)
admin.register(Payment)
