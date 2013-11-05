#encoding:utf-8
from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.models import User
from persons.models import Promoter, PromoterPhotos


class LoginForm(forms.Form):
    name = forms.CharField(max_length=30,
                           min_length=5,
                           required=True,
                           label='Nombre',
                           widget=forms.TextInput(attrs={'placeholder': 'Ej: JohnDoe',
                                                         'required': 'required'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': 'required'}),
                               label='Contraseña',
                               required=True,
                               max_length=30, min_length=6)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Ej: john',
                                               'required': 'required'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ej: johndoe@example.com',
                                            'required': 'required', 'type': 'email'}),
        }
    password = forms.CharField(max_length=20,
                               min_length=6,
                               widget=forms.PasswordInput(attrs={'required': 'required'}),
                               label='Contraseña',
                               required=True)
    repassword = forms.CharField(widget=forms.PasswordInput(attrs={'required': 'required'}),
                                 label='Repite Contraseña',
                                 required=True,
                                 max_length=30, min_length=6)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        repassword = cleaned_data.get('repassword')
        if password != repassword:
            raise forms.ValidationError("Las contrasenas no son iguales")
        return cleaned_data


class PromoterForm(forms.ModelForm):
    class Meta:
        model = Promoter
        widgets = {
            'ci': forms.TextInput(attrs={'placeholder': 'Ej: 55555',
                                         'required': 'required'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Ej: John',
                                                 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ej: Doe',
                                                'required': 'required'}),
            'age': widgets.AdminDateWidget(attrs={'placeholder': 'Ej: 02/12/1988'}),
            'mobile_phone': forms.TextInput(attrs={'placeholder': 'Ej: 0414-4403333',
                                                   'required': 'required'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ej: 0241-8885265'}),
            'address': forms.Textarea(attrs={'placeholder': 'Ej: Naguanagua',
                                             'rows': '3'}),
            'height': forms.TextInput(attrs={'placeholder': 'Ej: 1.80',
                                             'required': 'required'}),
            'weight': forms.TextInput(attrs={'placeholder': 'Ej: 80.1',
                                             'required': 'required'}),
            'pin': forms.TextInput(attrs={'placeholder': 'Ej: 55555'}),
        }

    measure1 = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number',
                                  'min': '40', 'max': '100'}),
                                  max_value=100,
                                  required=True,
                                  label='Busto')
    measure2 = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number',
                                  'min': '40', 'max': '100'}),
                                  max_value=100,
                                  required=True,
                                  label='Cintura')
    measure3 = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number',
                                  'min': '40', 'max': '100'}),
                                  max_value=100,
                                  required=True,
                                  label='Cadera')

    photo1 = forms.ImageField(label='Foto 1')
    photo2 = forms.ImageField(label='Foto 2')
