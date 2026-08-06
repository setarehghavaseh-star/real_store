from django.urls import path
from . import views
from .views import (LoginView,RegisterView,LogoutView,ProfileDashboardView)
from django.contrib.auth import views as auth_views
urlpatterns = [

    path("login/",LoginView.as_view(),name="login"),
    path("register/",RegisterView.as_view(),name="register"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("dashboard/",ProfileDashboardView.as_view(),name="dashboard"),
    path(
    "password-change/",
    auth_views.PasswordChangeView.as_view(
        template_name="accounts/password_change.html"
    ),
    name="password_change",
),

path(
    "password-change/done/",
    auth_views.PasswordChangeDoneView.as_view(
        template_name="accounts/password_change_done.html"
    ),
    name="password_change_done",
),
    


    path(
        "orders/",
        views.OrdersView.as_view(),
        name="orders"
    ),


    path(
        "favorites/",
        views.FavoritesView.as_view(),
        name="favorites"
    ),


    path(
        "addresses/",
        views.AddressesView.as_view(),
        name="addresses"
    ),


    path(
        "security/",
        views.SecurityView.as_view(),
        name="security"
    ),


    path(
        "settings/",
        views.SettingsView.as_view(),
        name="settings"
    ),

]