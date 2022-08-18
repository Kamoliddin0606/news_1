from django.urls import path
from .views import *
urlpatterns=[
    path('',index, name='index'),
    path('/<slug:slug>',index, name='index'),
    path('detail/<slug:slug>/', detail_post, name='detail_post')


]