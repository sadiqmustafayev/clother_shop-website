from django.shortcuts import render
from django.http import HttpResponse
from core.forms import ContactForm
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
  blogs = Blog.objects.filter(is_active=True).order_by("-created_at")
  context = {
    'title' : 'Blog Page',
    'blogs' : blogs,
    'blog_count' : blogs.count()
  }
  return render(request, 'blog.html', context=context)

def blog_details(request, blog_slug):
  blog = Blog.objects.get(slug = blog_slug)
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
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request, 'contact_us.html', context={'contact_form': ContactForm()})

  context = {
    'title' : 'Contact Us',
    'contact_form' : ContactForm(),
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

def faq(request):
  context = {
    'faqs' : FAQ.objects.filter(is_active=True)
   }
  return render(request, 'faq.html', context=context)
  

  