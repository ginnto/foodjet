from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('<slug:c_slug>/',views.home,name="prod_cat"),    #for view category wise
    path('<slug:c_slug>/<slug:product_slug>',views.prodDetails,name='details'),   # here two  arrgument
]