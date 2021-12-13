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


def submit(request):
    obj = Items()
    obj.name = request.POST.get('name')
    obj.price = request.POST.get('price')
    obj.description = request.POST.get('description')
    obj.quantity = request.POST.get('quantity')
    obj.cat = request.POST.get('cat')
    obj.save()
    #print(obj.name)
    mydict = {
        "name": obj.name,
        "price": obj.price,
        "description": obj.description,
        "quantity": obj.quantity,  
        "cat": obj.cat
    }

    return render(request, 'app1/additem.html', context=mydict)
