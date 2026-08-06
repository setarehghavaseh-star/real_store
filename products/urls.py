from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    ProductViewSet,
    ProductVariantViewSet,
    ProductImageViewSet,
    home,
    product_detail,
    CategoryDetailView,
    ProductListView
)

router = DefaultRouter()

router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)
router.register("variants", ProductVariantViewSet)
router.register("images", ProductImageViewSet)

urlpatterns = [

    path("", home, name="home"),

    path("product/<slug:slug>/",product_detail,name="product_detail",),

    path("api/", include(router.urls)),
    
    path("category/<slug:slug>/",CategoryDetailView.as_view(),name='category_detail'),
    
    path(
        "products/",
        ProductListView.as_view(),
        name="product_list"
    ),
]