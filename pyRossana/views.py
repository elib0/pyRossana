from django.template import RequestContext
from django.shortcuts import render
from persons import forms
from store import models


def home(request):
    num = 0
    form = forms.PromoterForm()
    products = models.Product.objects.all()
    categories = models.Categorie.objects.all()
    if request.user.is_authenticated():
        num = len(request.user.cart_set.filter(status=models.STATUS_CHOICES[0]))
    return render(request,
                  'index.html',
                  {'categories': categories, 'products': products,
                   'num': num, 'form': form},
                  context_instance=RequestContext(request))
