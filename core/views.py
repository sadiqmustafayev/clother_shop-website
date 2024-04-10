from django.shortcuts import render
from django.http import HttpResponse
from core.models import *

def index(request):
   context = {
    'title' : 'Home',
   }
   return render(request, 'index.html', context=context)
  
def about(request):
  context = {
    'title' : 'About',
   }
  return render(request, 'about.html', context=context)

def blog(request):
  context = {
    'title' : 'Blog Page',
    'blogs' : Blog.objects.filter(is_active=True).order_by("-created_at"),
  }
  return render(request, 'blog.html', context=context)

def blog_details(request, blog_id):
  blog = Blog.objects.get(id=blog_id)
  context = {
    'title' : blog.title,
    'blog' : blog
  }
  return render(request, 'blog-details.html', context=context)

def checkout(request):
  context = {
    'title' : 'CheckOut',
   }
  return render(request, 'checkout.html', context=context)

def contact_us(request):
  context = {
    'title' : 'Contact Us',
    'contact_us' : ContactUs.objects.filter(is_active=True).order_by("-created_at")
  }
  return render(request, 'contact_us.html', context=context)

def shop_details(request):
  context = {
    'title' : 'Shop Details',
   }
  return render(request, 'shop-details.html', context=context)

def shop(request):
  context = {
    'title' : 'Shop',
   }
  return render(request, 'shop.html', context=context)

def shopping_cart(request):
  context = {
    'title' : 'Shopping Cart',
   }
  return render(request, 'shopping-cart.html', context=context)
