from rest_framework import serializers

from library_app.models import Book, Borrowing, Payment


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "author", "cover", "inventory", "daily_fee")


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "author", "title")


class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book",
            "user",
        )


class BorrowingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ("id", "user", "book", "borrow_date", "expected_return_date")


class BorrowingDetailSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=False, read_only=True)

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "user",
            "book",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
        )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            "id",
            "status",
            "type",
            "borrowing",
            "session_url",
            "session_id",
            "payment_amount",
        )


class PaymentListSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="borrowing.user.id")

    class Meta:
        model = Payment
        fields = ("id", "user_id", "status", "payment_amount")


class PaymentDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="borrowing.user.id")
    borrowing = BorrowingDetailSerializer(many=False, read_only=True)

    class Meta:
        model = Payment
        fields = (
            "id",
            "user_id",
            "status",
            "type",
            "borrowing",
            "session_url",
            "payment_amount"
        )
