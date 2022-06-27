from django.shortcuts import render
from shop.models import *      #the models are in shop so we call the models in the shop
from django.db.models import Q


# Create your views here.


def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'qr':query,'pr':prod})