from django.shortcuts import render
from django.http import HttpResponse
from core.models import *

def index(request):
  return render(request, 'index.html')
  
def about(request):
  return render(request, 'about.html')

def blog_details(request):
  return render(request, 'blog-details.html')

def blog(request):
  context = {
    'blogs' : Blog.objects.filter(is_active=True).order_by("-created_at")
  }
  return render(request, 'blog.html', context=context)

def checkout(request):
  return render(request, 'checkout.html')

def contact_us(request):
  context = {
    'contact_us' : ContactUs.objects.filter(is_active=True).order_by("-created_at")
  }
  return render(request, 'contact_us.html', context=context)

def shop_details(request):
  return render(request, 'shop-details.html')

def shop(request):
  return render(request, 'shop.html')

def shopping_cart(request):
  return render(request, 'shopping-cart.html')
