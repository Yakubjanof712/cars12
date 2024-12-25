from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Comment


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True, label='Parolni takrorlash')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Parollar bir xil emas!")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
