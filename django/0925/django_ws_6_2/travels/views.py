from django.shortcuts import render, redirect
from .models import Travels
from .forms import TravelForm

# Create your views here.
def index(request):
    travels = Travels.objects.all()
    context = {
        'travels': travels,
    }
    return render(request, 'travels/index.html', context)

def create(request):
    if request.method == "POST":
        form = TravelForm(request.POST)
        if form.is_valid():
            travel = form.save()
            return redirect('travels:detail', travel.pk)

    else:
        form = TravelForm()
    context = {
        'form': form,
    }
    return render(request, 'travels/create.html', context)

def detail(request, pk):
    travel = Travels.objects.get(pk=pk)
    context = {
        'travel': travel,
    }
    return render(request, 'travels/detail.html', context)