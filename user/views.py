from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic import FormView, CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth.models import User
from . import forms
from django.urls import reverse_lazy
from user.models import Image
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Register(FormView):
    model = User
    form_class = forms.UserForm
    template_name = "user.html"

    def form_valid(self, form):
        res = super().form_valid(form)
        self.user = form.save()
        messages.success(self.request, "Sing Up Successfully !")
        return res

    def get_success_url(self):
        return reverse_lazy("register")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Sing Up"
        return context


class login(LoginView):
    template_name = "user.html"

    def get_success_url(self) -> str:
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, "Login Successfull")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Login information Wrong")
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login Now"
        return context


class logout(LogoutView):
    def get_success_url(self):
        messages.success(self.request, "Logout Successfully")
        return reverse_lazy("home")


class image(CreateView):
    form_class = forms.ImageForm
    template_name = "user.html"
    context_object_name = "image"

    def get_success_url(self):
        return reverse_lazy("home")

    def form_valid(self, form):
        res = super().form_valid(form)
        self.object.image = form.cleaned_data["image"]
        self.object.save()
        return res

@method_decorator(login_required, name='dispatch')
class upadate(UpdateView):
    model = User
    template_name = "upadate.html"
    form_class = forms.UserUpdateProfile
    pk_url_kwarg = "id"

    def get_success_url(self):
        messages.success(self.request, "profile update successfully")
        return reverse_lazy("home")


@login_required
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "password change successfully ")
            update_session_auth_hash(request, form.user)
            return redirect("home")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "pass.html", {"form": form, "type": "Password change now "})
