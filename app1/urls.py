from django.urls import path

from .views import*



urlpatterns=[
    path('',index,name='main page'),
    path('list/',showAllProducts,name='list'),
    path('addItem/', addItem, name="addItem"),
    path('editItem/<str:pk>/', editItem, name="editItem"),
    path('deleteItem/<str:pk>/', deleteItem, name="deleteItem"),
    
    
    
    #path('updateItem/<str:pk>/', updateItem, name="updateItem")
    
]