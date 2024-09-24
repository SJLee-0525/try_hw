from django.shortcuts import render, redirect
from .models import Restaurant

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants,
    }
    return render(request, 'restaurants/index.html', context)

def new(request):
    return render(request, 'restaurants/new.html')

def create(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    address = request.POST.get('address')
    tel = request.POST.get('tel')

    restaurant = Restaurant.objects.create(name=name, description=description, address=address, tel=tel)
    restaurant.save()

    return redirect("restaurants:index")