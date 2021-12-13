from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.lookups import In

# Create your models here.


class Category(models.Model):
    cat_name=CharField(max_length=100,blank=True)



class Items(models.Model):
    name=CharField(max_length=100,blank=True)
    price=IntegerField(blank=True)
    description=TextField(blank=True)
    quantity=IntegerField(blank=True)
    cat=models.ForeignKey(Category,related_name='category', on_delete=models.CASCADE,null=True)

