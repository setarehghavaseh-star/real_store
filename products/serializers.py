from rest_framework import serializers

from .models import (Category,Product,ProductImage,ProductVariant)



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields=[
            'id',
            'name',
            'slug',
            'image',
            'is_active'
        ]
        
        
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields =[
            'id',
            'image',
            'alt_text',
            'is_primary'
        ]
        
        
class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductVariant
        fields= [
            'id',
            'weight',
            'quality',
            'package_type',
            'price',
            'stock',
            'sku',
            'is_active'
        ]
        
        
        
class ProductSerializer(serializers.ModelSerializer):
    Category= CategorySerializer(read_only=True)
    variants=ProductVariantSerializer(
        many=True,
        read_only=True
    )
    images=ProductImageSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = Product
        
        fields = [
            'id',
            'name',
            'slug',
            'category',
            'short_description',
            'description',
            'main_image',
            'is_active',
            'is_featured',
            'average_rating',
            'variants',
            'images',
            'created_at',
            'updated_at'
        ]