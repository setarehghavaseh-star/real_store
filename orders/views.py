from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.models import Cart
from .models import Order


class CheckoutView(LoginRequiredMixin, View):

    template_name = "orders/checkout.html"

    def get(self, request):
        cart = get_object_or_404(
            Cart,
            session_key=request.session.session_key
        )
        return render(request, self.template_name, {"cart": cart})

    def post(self, request):
        cart = get_object_or_404(
            Cart,
            session_key=request.session.session_key
        )

        # اگه قبلاً برای این سبد سفارش ساخته شده، دوباره نساز
        order, created = Order.objects.get_or_create(
            cart=cart,
            defaults={
                "user": request.user,
                "total_price": cart.total_price,
            }
        )

        return redirect("payment", order_id=order.id)


class OrderSuccessView(TemplateView):
    template_name = "orders/success.html"

class PaymentView(LoginRequiredMixin, View):

    def get(self, request, order_id):

        order = get_object_or_404(
            Order,
            id=order_id,
            user=request.user
        )


        return render(
            request,
            "orders/payment.html",
            {
                "order": order
            }
        )



    def post(self, request, order_id):

        order = get_object_or_404(
            Order,
            id=order_id,
            user=request.user
        )


        order.payment_code = request.POST.get(
            "payment_code"
        )


        if request.FILES.get("payment_image"):

            order.payment_image = request.FILES.get(
                "payment_image"
            )


        order.save()


        return redirect(
            "order_success"
        )