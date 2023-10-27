from django.urls import include, path
from rest_framework import routers

from library_app.views import BookViewSet, BorrowingViewSet, PaymentViewSet

router = routers.DefaultRouter()

router.register("books", BookViewSet)
router.register("borrowings", BorrowingViewSet)
router.register("payments", PaymentViewSet)


urlpatterns = [path("", include(router.urls))]


app_name = "library"
