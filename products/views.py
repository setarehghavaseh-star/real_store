from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Product
from .models import Category
from django.views.generic import ListView
from .models import Product


from django.views.generic import ListView
from django.db.models import Q



from .models import (
    Category,
    Product,
    ProductVariant,
    ProductImage,
)

from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductVariantSerializer,
    ProductImageSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(
        is_active=True
    ).prefetch_related(
        "variants",
        "images"
    )

    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class ProductVariantViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.filter(
        is_active=True
    )

    serializer_class = ProductVariantSerializer
    permission_classes = [AllowAny]


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()

    serializer_class = ProductImageSerializer
    permission_classes = [AllowAny] 
    





def home(request):
    products = Product.objects.filter(
        is_active=True
    ).prefetch_related(
        "variants",
        "images"
    )
    categories= Category.objects.all()
    context = {
        "products": products,
        'categories':categories,
    }

    return render(
        request,
        "products/index.html",
        context
    )


def product_detail(request, slug):
    product = get_object_or_404(
        Product.objects.prefetch_related(
            "variants",
            "images"
        ),
        slug=slug,
        is_active=True
    )

    context = {
        "product": product,
    }

    return render(
        request,
        "products/product_detail.html",
        context
    )
    
    
    
from django.views.generic import DetailView
from .models import Category


class CategoryDetailView(DetailView):

    model = Category

    template_name = "products/category_detail.html"

    context_object_name = "category"


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["products"] = self.object.products.filter(
            is_active=True
        )

        return context
    
    


class ProductListView(ListView):

    model = Product

    template_name = "products/product_list.html"

    context_object_name = "products"


    def get_queryset(self):

        products = Product.objects.all()

        query = self.request.GET.get("q")


        if query:

            words = query.split()

            search_filter = Q()

            for word in words:

                search_filter |= (
                    Q(name__icontains=word) |
                    Q(description__icontains=word)
                )


            products = products.filter(search_filter)


        return products
