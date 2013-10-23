from django.shortcuts import render
from persons import forms


def home(request):
    form1 = forms.PersonForm()
    form2 = forms.PromoterForm()
    return render(request, 'index.html', {'form1': form1, 'form2': form2})
