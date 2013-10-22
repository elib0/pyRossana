from django import forms
from django.contrib.auth.models import User
from persons.models import Promoter


class LoginForm(forms.Form):
    name = forms.CharField(max_length=30, min_length=5, required=True, label='Nombre')
    password = forms.CharField(widget=forms.PasswordInput(),
                               label='Contrasena',
                               required=True,
                               max_length=30, min_length=6)


class PersonForm(forms.ModelForm):
    class Meta:
        model = User

    repassword = forms.CharField(widget=forms.PasswordInput(),
                                 label='Repite Contrasena',
                                 required=True,
                                 max_length=30, min_length=6)

    def clean(self):
        cleaned_data = super(PersonForm, self).clean()
        password = cleaned_data.get('password')
        repassword = cleaned_data.get('repassword')
        if password != repassword:
            raise forms.ValidationError("Las contrasenas no son iguales")
        return cleaned_data


# class PersonForm(forms.ModelForm):
#     cid = forms.IntegerField(max_value=9, min_value=8, required=True, label='Cedula')
#     loginname = forms.CharField(max_length=20,
#                                 min_length=6,
#                                 required=True,
#                                 label='Nombre Usuario')
#     name = forms.CharField(max_length=30, min_length=2, required=True, label='Nombre')
#     last_name = forms.CharField(max_length=30,
#                                 min_length=3,
#                                 required=True,
#                                 label='Apellido')
#     email = forms.CharField(max_length=100,
#                             min_length=10,
#                             required=True,
#                             label='Correo Electronico')
#     password = forms.CharField(widget=forms.PasswordInput(),
#                                label='Contrasena',
#                                required=True,
#                                max_length=30, min_length=6)
#     repassword = forms.CharField(widget=forms.PasswordInput(),
#                                  label='Repite Contrasena',
#                                  required=True,
#                                  max_length=30, min_length=6)
#     mobile_phone = forms.CharField(max_length=12, min_length=11, label='Telefono')
#     address = forms.CharField(max_length=200,
#                               min_length=10,
#                               widget=forms.Textarea(),
#                               label='Direccion')

    # def clean(self):
    #     cleaned_data = super(RegisterUserForm, self).clean()
    #     password = cleaned_data.get('password')
    #     repassword = cleaned_data.get('repassword')
    #     if password != repassword:
    #         raise forms.ValidationError("Las contrasenas no son iguales")
    #     return cleaned_data


class PromoterForm(forms.ModelForm):
    class Meta:
        model = Promoter
