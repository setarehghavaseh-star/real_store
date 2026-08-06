from django.db import models
from products.models import ProductVariant


class Cart(models.Model):
    session_key=models.CharField(
        max_length=100,
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True) 
    
    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())
    
    def __str__(self):
        return self.session_key
    
    
    
    
class CartItem(models.Model):
    cart=models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )
    variant=models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE
    )
    
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_price(self):
        return self.variant.price * self.quantity
    
    
    def __str__(self):
        return self.variant.name
    
    
    