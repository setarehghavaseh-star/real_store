from django.urls import path

from .views import (
    AddToCartView,
    CartDetailView
)
from .views import (
    RemoveCartItemView,
    IncreaseCartItemView,
    DecreaseCartItemView,
    CartDetailView
)


urlpatterns = [
    path(
        "add/<int:pk>/",
        AddToCartView.as_view(),
        name="add_to_cart"
    ),
    path(
        "",
        CartDetailView.as_view(),
        name="cart_detail"
    ),

    path(
    "remove/<int:pk>/",
    RemoveCartItemView.as_view(),
    name="remove_cart_item"
),
    path(
    "increase/<int:pk>/",
    IncreaseCartItemView.as_view(),
    name="increase_cart_item"
),
    path(
    "decrease/<int:pk>/",
    DecreaseCartItemView.as_view(),
    name="decrease_cart_item"
),
]