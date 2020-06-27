from django.urls import path
from . import views

#url mapping
urlpatterns=[
    path('',views.index,name='index')]