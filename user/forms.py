from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import EmailInput, TextInput, FileInput, Select

from home.models import UserProfile


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields =('username','email','first_name', 'last_name')
        widgets = {
         'username' : TextInput(attrs={'class':'input','placeholder':'username'}),
         'email': EmailInput(attrs={'class':'input','placeholder':'email'}),
         'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
         'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),

       }


CITY = [
    ('Istanbul','Istanbul'),
    ('Ankara','Ankara'),
    ('Izmir', 'Izmir'),
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'adress', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'adress': EmailInput(attrs={'class': 'input', 'placeholder': 'adress'}),
            'city': Select(attrs={'class': 'input','placeholder': 'city'}, choices=CITY),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),

        }
