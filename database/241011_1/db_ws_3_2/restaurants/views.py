from django.shortcuts import render, redirect
from .models import Menu, Category, Restaurant
from .forms import RestaurantForm

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants,
    }
    return render(request, 'restaurants/index.html', context)

def create_restaurant(request):
    if request.method == 'POST':
        restaurant_form = RestaurantForm(request.POST)
        if restaurant_form.is_valid():
            restaurant_form.save()
            return redirect('restaurants:index')
    restaurant_form = RestaurantForm()
    context = {
        'restaurant_form': restaurant_form,
    }
    return render(request, 'restaurants/create.html', context)

def detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    context = {
        'restaurant': restaurant,
    }
    return render(request, 'restaurants/detail.html', context)