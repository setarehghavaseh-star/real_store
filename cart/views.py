from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from products.models import Product
from .models import Cart, CartItem
from products.models import ProductVariant



class AddToCartView(View):

    def get(self, request, pk):

        variant = get_object_or_404(
            ProductVariant,
            id=pk
        )


        cart, created = Cart.objects.get_or_create(
            session_key=request.session.session_key
        )
        item, created = CartItem.objects.get_or_create(
            cart=cart,
            variant=variant
        )
        if not created:
            item.quantity += 1
            item.save()
        return redirect("cart_detail")

class RemoveCartItemView(View):
    def get(self, request, pk):
        item = get_object_or_404(
            CartItem,
            id=pk
        )
        item.delete()
        return redirect("cart_detail")
class IncreaseCartItemView(View):
    def get(self, request, pk):
        item = get_object_or_404(
            CartItem,
            id=pk
        )
        item.quantity += 1
        item.save()
        return redirect("cart_detail")
class DecreaseCartItemView(View):
    def get(self, request, pk):
        item = get_object_or_404(
            CartItem,
            id=pk
        )
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()
        return redirect("cart_detail")
class CartDetailView(View):
    def get(self, request):
        if not request.session.session_key:
            request.session.create()
        session_key=request.session.session_key
        cart, created = Cart.objects.get_or_create(
            session_key=session_key
        )
        items = CartItem.objects.filter(cart=cart)
        return render(request, "cart/cart_detail.html", {"cart": cart, "items": items})
