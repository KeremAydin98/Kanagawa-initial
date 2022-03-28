from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):

        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'sex', 'area_code', 'phone_number' )

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):

        model = CustomUser
        fields = UserChangeForm.Meta.fields