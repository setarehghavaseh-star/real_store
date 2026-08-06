from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):

    username = None

    phone_number = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="شماره موبایل"
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    USERNAME_FIELD = "phone_number"

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number


class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    bio = models.TextField(blank=True)

    birth_date = models.DateField(
        blank=True,
        null=True
    )

    province = models.CharField(
        max_length=100,
        blank=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    postal_code = models.CharField(
        max_length=10,
        blank=True
    )

    address = models.TextField(blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.user.phone_number