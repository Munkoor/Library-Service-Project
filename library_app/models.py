from django.db import models
from django.conf import settings


class Book(models.Model):
    class CoverChoices(models.TextChoices):
        HARD = "Hard"
        SOFT = "Soft"

    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    cover = models.CharField(max_length=8, choices=CoverChoices.choices)
    inventory = models.PositiveIntegerField(null=True, default=1)
    daily_fee = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.author} - {self.title}"


class Borrowing(models.Model):
    borrow_date = models.DateField()
    expected_return_date = models.DateField()
    actual_return_date = models.DateField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book}, {self.borrow_date}({self.id})"


class Payment(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "Pending"
        Paid = "Paid"

    class TypeChoices(models.TextChoices):
        PAYMENT = "Payment"
        FINE = "Fine"

    status = models.CharField(max_length=10, choices=StatusChoices.choices)
    type = models.CharField(max_length=10, choices=TypeChoices.choices)
    borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE,
                                  related_name="payments")
    session_url = models.URLField(max_length=250, null=True, blank=True)
    session_id = models.CharField(max_length=10, null=True, blank=True)
    payment_amount = models.IntegerField(default=0)

    def __str__(self):
        return f"Payment #{self.id}, status: {self.status}"
