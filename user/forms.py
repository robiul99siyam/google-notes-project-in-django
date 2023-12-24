from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User
from django import forms
from user.models import Image

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
class UserUpdateProfile (UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


