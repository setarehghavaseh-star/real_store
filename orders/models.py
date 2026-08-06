from django.db import models
from accounts.models import User
from cart.models import Cart


class Order(models.Model):

    STATUS = (
        ("pending", "در انتظار پرداخت"),
        ("paid", "پرداخت شده"),
        ("sent", "ارسال شده"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders",
    )

    cart = models.OneToOneField(
        Cart,
        on_delete=models.CASCADE,
    )

    total_price = models.PositiveIntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="pending",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Order #{self.id}"
    
    
payment_code = models.CharField(
    max_length=100,
    blank=True,
    null=True
)


payment_image = models.ImageField(
    upload_to="payments/",
    blank=True,
    null=True
)
