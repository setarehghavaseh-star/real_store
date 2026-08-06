from django.contrib import admin
from .models import Cart,CartItem


class CartItemInline(admin.TabularInline):
    model= CartItem
    extra=0
    readonly_fields=(
        'variant',
        'quantity'
    )
    
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=('session_key','created_at')
    
    inlines=[CartItemInline,]