#encoding:utf-8
from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.models import User
from persons.models import Promoter


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


class ProfileForm(forms.Form):
    dni = forms.CharField(max_length=9,
                          min_length=3,
                          required=True,
                          label='Cedula',
                          widget=forms.TextInput(attrs={'placeholder': 'Ej: 18058666',
                                                        'required': 'required'})
                          )
    first_name = forms.CharField(max_length=30, min_length=2,
                                 label='Nombre',
                                 widget=forms.TextInput(attrs={'placeholder': 'Carlos',
                                                        'required': 'required'}))
    last_name = forms.CharField(max_length=30, min_length=2,
                                label='Apellido',
                                widget=forms.TextInput(attrs={'placeholder': 'Gomez',
                                                              'required': 'required'})
                                )
    email = forms.EmailField()
    phone = forms.CharField(max_length=12,
                            min_length=11,
                            label='Teléfono personal',
                            widget=forms.TextInput(attrs={'placeholder': 'Ej: 0414-4403333','required': 'required'}))
    adress = forms.CharField(label='Dirección de facturación',
                             widget=forms.Textarea(attrs={'placeholder': 'Ej: Naguanagua',
                                                          'rows': '3'})
                             )


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(
                                   attrs={'required': 'required'}),
                                   label='Contraseña Antigua',
                                   required=True,
                                   max_length=30, min_length=6)
    new_password = forms.CharField(widget=forms.PasswordInput(
                                   attrs={'required': 'required'}),
                                   label='Contraseña Nueva',
                                   required=True,
                                   max_length=30, min_length=6)
    renew_password = forms.CharField(widget=forms.PasswordInput(
                                     attrs={'required': 'required'}),
                                     label='Repita Contraseña Nueva',
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
    repassword = forms.CharField(widget=forms.PasswordInput(
                                 attrs={'required': 'required'}),
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
    status = forms.IntegerField(initial=0, widget=forms.HiddenInput())
