from django.http.response import HttpResponse
from django.shortcuts import render
from .models import*
# Create your views here.
def index(request):
   
    items=Items.objects.all()
    context={
        "items" : items,
    }
    return render(request,'app1/index.html', context=context,)