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


def addItem(request):
    obj = Items()
    if request.method == 'POST':
        #print('Printing POST request: ', request.POST)
        obj.name = request.POST.get('name')
        obj.description = request.POST.get('description')
        obj.price = request.POST.get('price')
        obj.quantity = request.POST.get('quantity')
        obj.cat = request.POST.get('cat')
        obj.save()

    return render(request, 'app1/additem.html')
