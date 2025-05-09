from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class customUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'is_active', 'is_admin', 'is_staff']

class customUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'is_active', 'is_admin', 'is_staff']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    choose_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']

    def clean_choose_password(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('choose_password')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords do not match")
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_active = True
        if commit:
            user.save()
        return user
class loginForm(forms.Form):
    email = forms.EmailField(label="email")
    password = forms.CharField(label="password",widget=forms.PasswordInput())
    
