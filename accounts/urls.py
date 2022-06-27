from django.urls import path
from . import views

urlpatterns=[
    path('log_in',views.login,name='log_in'),
    path('reg',views.register,name='reg'),

    path('log_out',views.logout,name='log_out')


]
