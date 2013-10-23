from django.shortcuts import render
from persons import forms
from store import models


def home(request):
    # form1 = forms.PersonForm()
    # form2 = forms.PromoterForm()
    products = models.Product.objects.all()
    if request.user.is_authenticated():
        num = len(request.user.cart_set.filter(status=models.STATUS_CHOICES[0]))
    else:
        num = 0
    return render(request, 'index.html', {'products': products, 'num': num})
