#encoding:utf-8
from django import forms
from django.contrib.auth.models import User
from persons.models import Promoter


class LoginForm(forms.Form):
    name = forms.CharField(max_length=30, 
                           min_length=5, 
                           required=True, 
                           label='Nombre',
                           widget=forms.TextInput(attrs={'placeholder':'Ej: JohnDoe'}))
    password = forms.CharField(widget=forms.PasswordInput(),
                               label='Contraseña',
                               required=True,
                               max_length=30, min_length=6)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('last_login',
                   'is_superuser',
                   'groups',
                   'user_permissions',
                   'is_staff',
                   'is_active',
                   'date_joined',)
    ci = forms.IntegerField(max_value=9, min_value=8, label='Cedula')
    repassword = forms.CharField(widget=forms.PasswordInput(),
                                 label='Repite Contraseña',
                                 required=True,
                                 max_length=30, min_length=6)

    def clean(self):
        cleaned_data = super(PersonForm, self).clean()
        password = cleaned_data.get('password')
        repassword = cleaned_data.get('repassword')
        if password != repassword:
            raise forms.ValidationError("Las Contraseñas no son iguales")
        return cleaned_data


class PromoterForm(forms.ModelForm):
    class Meta:
        model = Promoter
        widgets ={
            'ci': forms.TextInput(attrs={'placeholder': 'Ej: 55555'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Ej: John'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ej: Doe'}),
            'age': forms.TextInput(attrs={'placeholder': 'Ej: 55555'}),
            'mobile_phone': forms.TextInput(attrs={'placeholder': 'Ej: 0414-4403333'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ej: 0241-8885265'}),
            'address': forms.TextInput(attrs={'placeholder': 'Ej: Trigal Norte'}),
            'height': forms.TextInput(attrs={'placeholder': 'Ej: 1.80'}),
            'weight': forms.TextInput(attrs={'placeholder': 'Ej: 80.1'}),
            'pin': forms.TextInput(attrs={'placeholder': 'Ej: 55555'}),
        }
