from django.shortcuts import render, get_object_or_404
from .models import Category, Student, Media, Team



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    students = Student.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        students = Student.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'students': students
    }
    return render(request, 'shop/product/list.html', context)


def media_list(request,):
    medias = Media.objects.all


    context = {
        'medias': medias
    }
    return render(request, 'shop/product/media.html', context)


def team_list(request,):
    teams = Team.objects.all


    context = {
        'teams': teams
    }
    return render(request, 'shop/product/team.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Student, id=id, slug=slug, available=True)
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



def team(request):
  return render(request, 'shop/product/team.html')

def donate(request):
  return render(request, 'shop/product/donate.html')

def contact(request):
  return render(request, 'shop/product/contact.html')

  
