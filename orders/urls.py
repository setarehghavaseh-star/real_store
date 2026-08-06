from django.urls import path

from .views import (
    CheckoutView,
    OrderSuccessView,
    PaymentView,
)


urlpatterns = [

    path(
        "checkout/",
        CheckoutView.as_view(),
        name="checkout"
    ),


    path(
        "success/",
        OrderSuccessView.as_view(),
        name="order_success"
    ),


    path(
        "payment/<int:order_id>/",
        PaymentView.as_view(),
        name="payment"
    ),

]
