from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Profile


class RegisterForm(UserCreationForm):

    class Meta:

        model = User

        fields = [

            "phone_number",

            "first_name",

            "last_name",

            "email",

            "password1",

            "password2",

        ]

        widgets = {

            "phone_number": forms.TextInput(attrs={
                "placeholder": "شماره موبایل"
            }),

            "first_name": forms.TextInput(attrs={
                "placeholder": "نام"
            }),

            "last_name": forms.TextInput(attrs={
                "placeholder": "نام خانوادگی"
            }),

            "email": forms.EmailInput(attrs={
                "placeholder": "ایمیل (اختیاری)"
            }),

        }


class UserUpdateForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [

            "first_name",

            "last_name",

            "email",

        ]


class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model = Profile

        fields = [

            "profile_image",

            "bio",

            "birth_date",

            "province",

            "city",

            "postal_code",

            "address",

        ]
