from rest_framework import viewsets

from library_app.models import Book, Borrowing
from library_app.serializers import BookSerializer, BookListSerializer, \
    BorrowingSerializer, BorrowingListSerializer, BorrowingDetailSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return BookListSerializer

        return BookSerializer


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

    def get_queryset(self):
        queryset = self.queryset

        if self.action == "list" or "retrieve":
            queryset = queryset.select_related("book")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer

        if self.action == "retrieve":
            return BorrowingDetailSerializer

        return BorrowingSerializer