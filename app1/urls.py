from django.urls import path

from .views import*



urlpatterns=[
    path('',index,name='main page'),
    path('list',index,name='list'),
    path('addItem', addItem, name="addItem")
    
]