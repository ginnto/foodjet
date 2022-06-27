from django.shortcuts import render,get_object_or_404
from . models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def home(request,c_slug=None):
    c_page=None
    pro=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        pro=products.objects.filter(category=c_page,available=True)
    else:

        pro=products.objects.all().filter(available=True)
    cat=categ.objects.all()
    paginator=Paginator(pro,6)      #6 represent how many items u want to display in home
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1
    try:
        proe=paginator.page(page)
    except(EmptyPage,InvalidPage):
        proe=paginator.page(paginator.num_pages)

    return render(request,'home.html',{'results':pro,'ct':cat,'pr':proe})

def prodDetails(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'pr':prod})
