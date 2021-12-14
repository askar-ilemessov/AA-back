from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import*
# Create your views here.
def index(request):
   
    items=Items.objects.all()
    context={
        "items" : items,
    }
    return render(request,'app1/list.html', context=context,)


def showAllProducts(request):
    items=Items.objects.order_by('price')
    context={
        "items" : items,
    }
    return render(request,'app1/list.html', context=context)



def addItem(request):
    obj = Items()
    if request.method == 'POST':
        #print('Printing POST request: ', request.POST)
        obj.name = request.POST.get('name')
        obj.description = request.POST.get('description')
        obj.price = request.POST.get('price')
        obj.quantity = request.POST.get('quantity')
        obj.category = request.POST.get('category')
        obj.save()

    return render(request, 'app1/additem2.html')


def editItem(request, pk):
    obj = Items.objects.get(id=pk)

    mydict = {
        "name": obj.name,
        "description": obj.description,
        "price": obj.price,
        "quantity": obj.quantity,
        "category": obj.category,   
    }

    if request.method == 'POST':
        #print('Printing POST request: ', request.POST)
        obj.name = request.POST.get('name')
        obj.description = request.POST.get('description')
        obj.price = request.POST.get('price')
        obj.quantity = request.POST.get('quantity')
        obj.category = request.POST.get('category')
        obj.save()
        return redirect('/')
    return render(request, 'app1/editItem2.html', context=mydict)


def deleteItem(request, pk):
    obj = Items.objects.get(id=pk)
    obj.delete()
    mydict = {
        "items": Items.objects.order_by('-id')
    }
    return render(request, 'app1/list.html', context=mydict)

''' 
def updateItem(request, pk):
    obj = Items.objects.get(id=pk)

    obj.name = request.POST.get('name')
    obj.description = request.POST.get('description')
    obj.price = request.POST.get('price')
    obj.quantity = request.POST.get('quantity')
    obj.category = request.POST.get('category')
    obj.save()

    mydict = {
        "allitems": Items.objects.order_by('-id')
    }

    return render(request, 'app1/index.html', content=mydict)
'''