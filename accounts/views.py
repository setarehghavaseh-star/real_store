from django.contrib.auth import login, logout

from django.contrib.auth.views import LoginView as DjangoLoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect

from django.urls import reverse_lazy

from django.views.generic import CreateView, TemplateView

from .forms import *

from .models import Profile



class LoginView(DjangoLoginView):

    template_name = "accounts/login.html"

    redirect_authenticated_user = True

    def get_success_url(self):

        return self.request.GET.get("next") or reverse_lazy("home")


class RegisterView(CreateView):

    template_name = "accounts/register.html"

    form_class = RegisterForm

    def form_valid(self, form):

        response = super().form_valid(form)

        login(self.request, self.object)

        return response

    def get_success_url(self):

        return reverse_lazy("home")


class LogoutView(DjangoLoginView):

    def get(self, request):

        logout(request)

        return redirect("home")


class ProfileDashboardView(LoginRequiredMixin, TemplateView):

    template_name = "accounts/dashboard.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        profile, created = Profile.objects.get_or_create(
            user=self.request.user
        )

        context["profile"] = profile

        context["user_form"] = UserUpdateForm(
            instance=self.request.user
        )

        context["profile_form"] = ProfileUpdateForm(
            instance=profile
        )

        return context

    def post(self, request, *args, **kwargs):

        profile, created = Profile.objects.get_or_create(
            user=request.user
        )

        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()

            profile_form.save()

            return redirect("dashboard")

        return self.render_to_response({

            "profile": profile,

            "user_form": user_form,

            "profile_form": profile_form,

        })



class OrdersView(LoginRequiredMixin, TemplateView):

    template_name = "accounts/orders.html"



class FavoritesView(LoginRequiredMixin, TemplateView):

    template_name = "accounts/favorites.html"



class AddressesView(LoginRequiredMixin, TemplateView):

    template_name = "accounts/addresses.html"



class SecurityView(LoginRequiredMixin, TemplateView):

    template_name = "accounts/security.html"



class SettingsView(LoginRequiredMixin, TemplateView):

    template_name = "accounts/settings.html"
    
    
    

