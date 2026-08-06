from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="نام دسته‌بندی"
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    image = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="دسته‌بندی"
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام محصول"
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    short_description = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="توضیح کوتاه"
    )

    description = models.TextField(
        verbose_name="توضیحات"
    )

    main_image = models.ImageField(
        upload_to="products/main/",
        blank=True,
        null=True,
        verbose_name="عکس اصلی"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="محصول ویژه"
    )

    average_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)
        
        
        
        
class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variants",
        verbose_name="محصول"
    )

    weight = models.CharField(
        max_length=50,
        verbose_name="وزن"
    )

    quality = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="کیفیت"
    )

    package_type = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="نوع بسته‌بندی"
    )

    price = models.PositiveIntegerField(
        verbose_name="قیمت"
    )

    stock = models.PositiveIntegerField(
        default=0,
        verbose_name="موجودی"
    )

    sku = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="SKU"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "تنوع محصول"
        verbose_name_plural = "تنوع‌های محصول"
        ordering = ["price"]

    def __str__(self):
        return f"{self.product.name} - {self.weight}"   
        
        
        
        
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="محصول"
    )

    image = models.ImageField(
        upload_to="products/gallery/",
        verbose_name="تصویر"
    )

    alt_text = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن جایگزین"
    )

    is_primary = models.BooleanField(
        default=False,
        verbose_name="عکس اصلی"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "تصویر محصول"
        verbose_name_plural = "تصاویر محصول"

    def __str__(self):
        return f"تصویر {self.product.name}"
        
        
        