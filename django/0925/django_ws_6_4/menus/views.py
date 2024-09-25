from django.shortcuts import render, redirect
from .models import Menu
from .forms import MenuForm

# Create your views here.
def index(request):
    menus = Menu.objects.order_by('-price')
    context = {
        'menus': menus
    }
    return render(request, 'menus/index.html', context)

def detail(request, menu_pk):
    menu = Menu.objects.get(pk=menu_pk)
    context = {
        'menu': menu
    }
    return render(request, 'menus/detail.html', context)

# def new(request):
#     form = MenuForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'menus/new.html', context)

def create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save()
            return redirect('menus:detail', menu.pk)
    else:
        form = MenuForm()
    context = {
        'form': form
    }
    return render(request, 'menus/new.html', context)
    
# def edit(request, menu_pk):
    # menu = Menu.objects.get(pk=menu_pk)
    # form = MenuForm(instance=menu)
    # context = {
    #     'menu': menu,
    #     'form': form
    # }
    # return render(request, 'menus/edit.html', context)

def update(request, menu_pk):
    menu = Menu.objects.get(pk=menu_pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            menu = form.save()
            return redirect('menus:detail', menu.pk)
    else:
        form = MenuForm(instance=menu)
    context = {
        'menu': menu,
        'form': form
    }
    return render(request, 'menus/edit.html', context)
    
def delete(request, menu_pk):
    menu = Menu.objects.get(pk=menu_pk)
    if request.method == 'POST':
        menu.delete()
        return redirect('menus:index')
    else:
        return redirect('menus:detail', menu.pk)