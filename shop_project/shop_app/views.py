from django.shortcuts import render
from .models import Item

def shop(request):
    items = Item.objects.all()
    return render(request, 'shop.html', {'items' : items})


# Create your views here.
