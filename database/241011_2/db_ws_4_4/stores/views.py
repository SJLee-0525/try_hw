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
    products_form = ProductForm()
    context = {
        'store': store,
        'products': products,
        'products_form': products_form
    }
    return render(request, 'stores/detail.html', context)

def stores_create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save()
            return redirect('stores:detail', store.pk)
    else:
        form = StoreForm()
    context = {
        'form': form
    }
    return render(request, 'stores/stores_create.html', context)

def products_create(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    if request.method == 'POST':
        products_form = ProductForm(request.POST)
        if products_form.is_valid():
            product = products_form.save(commit=False)
            product.store = store
            product.user = request.user
            product.save()
        else:
            context = {
                'store': store,
                'products_form': products_form
            }
            return render(request, 'stores/detail.html', context)
    return redirect('stores:detail', store.pk)

def delete_product(request, store_pk, product_pk):
    product = Product.objects.get(pk=product_pk)
    if request.user == product.user:
        product.delete()
    return redirect('stores:detail', store_pk)