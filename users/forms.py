from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from users.models import UserProfile


class SignUpForm(UserCreationForm):

    username = forms.CharField(
        max_length=30,
        label='Kullanıcı Adı',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Kullanıcı adı'
        })
    )

    email = forms.EmailField(
        max_length=200,
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email adresi'
        })
    )

    first_name = forms.CharField(
        max_length=100,
        label='İsim',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'İsim'
        })
    )

    last_name = forms.CharField(
        max_length=100,
        label='Soyisim',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Soyisim'
        })
    )

    password1 = forms.CharField(
        label='Şifre',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Şifre'
        })
    )

    password2 = forms.CharField(
        label='Şifre Tekrar',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Şifre tekrar'
        })
    )

    class Meta:
        model = User

        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

class UserUpdateForm(UserChangeForm):

    password = None

    class Meta:
        model = User

        fields = (
            'username',
            'email',
            'first_name',
            'last_name'
        )

        widgets = {

            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Kullanıcı Adı'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),

            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'İsim'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Soyisim'
            }),

        }


CITY = [
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),
]


class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model = UserProfile

        fields = (
            'phone',
            'address',
            'city',
            'country',
            'image',
            'language'
        )

        widgets = {

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefon'
            }),

            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Adres'
            }),

            'city': forms.Select(attrs={
                'class': 'form-select'
            }, choices=CITY),

            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ülke'
            }),

            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),

            'language': forms.Select(attrs={
                'class': 'form-select'
            }),

        }