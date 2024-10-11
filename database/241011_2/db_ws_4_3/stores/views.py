from django.shortcuts import render, redirect
from .models import Store, Product
from .forms import StoreForm, ProductForm

# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores': stores
    }
    return render(request, 'stores/index.html', context)

def detail(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    products = store.product_set.all()
    product_form = ProductForm()
    context = {
        'product_form': product_form,
        'products': products,
        'store': store
    }
    return render(request, 'stores/detail.html', context)

def create_store(request):
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save()
            return redirect('stores:detail', store.pk)
    else:
        form = StoreForm()
    context = {
        'form': form,
    }
    return render(request, 'stores/create_store.html', context)

def add_product(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    product_form = ProductForm(request.POST)
    if product_form.is_valid():
        product = product_form.save(commit=False)
        product.store = store
        product.user = request.user
        product_form.save()
        return redirect('stores:detail', store_pk)
    context = {
        'store': store,
        'product_form': product_form,
    }
    return render(request, 'stores/detail.html', context)