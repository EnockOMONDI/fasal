from django.shortcuts import render, get_object_or_404
from .models import Category, Product



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)


def home(request):
  return render(request, 'shop/product/home.html')

def about(request):
  return render(request, 'shop/product/about.html')

def projects(request):
  return render(request, 'shop/product/projects.html')

def media(request):
  return render(request, 'shop/product/media.html')

def team(request):
  return render(request, 'shop/product/team.html')

def donate(request):
  return render(request, 'shop/product/team.html')

def contact(request):
  return render(request, 'shop/product/team.html')

  
