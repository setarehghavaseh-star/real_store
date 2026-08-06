from django.contrib import admin

from .models import (
    Category,
    Product,
    ProductVariant,
    ProductImage,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_active",
        "created_at",
        'updated_at'
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "is_active",
        "is_featured",
        "average_rating",
        "created_at",
        'updated_at'
    )

    list_filter = (
        "category",
        "is_active",
        "is_featured",
    )

    search_fields = (
        "name",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "weight",
        "quality",
        "package_type",
        "price",
        "stock",
        "sku",
        "is_active",
    )

    list_filter = (
        "is_active",
        "quality",
        "package_type",
    )

    search_fields = (
        "product__name",
        "sku",
        "weight",
    )

    list_editable = (
        "price",
        "stock",
        "is_active",
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "is_primary",
        "created_at",
    )

    list_filter = (
        "is_primary",
    )

    search_fields = (
        "product__name",
    )