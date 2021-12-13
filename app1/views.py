from django.http.response import HttpResponse
from django.shortcuts import render
from .models import*
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return checker(request)
        else:
            messages.error(request,'Введен неверный логин или пароль')
            return render(request,'app1/signin.html')
    else:
        return render(request,'app1/signin.html')

def checker(request):
    items=Items.objects.all()
    context={
        "items" : items,
    }
    return render(request,'app1/index.html', context=context,)









    # items=Items.objects.all()
    # context={
    #     "items" : items,
    # }
    # return render(request,'app1/index.html', context=context,)