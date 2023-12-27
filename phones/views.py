from django.http import HttpResponse
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones: list[Phone] = list(Phone.objects.all())

    if request.GET.get('sort') == 'name':
        phones.sort(key=lambda x: x.name)
    elif request.GET.get('sort') == 'min_price':
        phones.sort(key=lambda x: x.price)
    elif request.GET.get('sort') == 'max_price':
        phones.sort(key=lambda x: x.price, reverse=True)

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
