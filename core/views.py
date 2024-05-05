# from pyexpat.errors import messages
from django.contrib import messages
from django.views.generic import ListView  
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.forms import ShopCommentForm, ContactForm
from core.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
    user_input = ""

    # Arama işlemi POST isteği ile yapılıyorsa
    if request.method == 'POST':
        user_input = request.POST.get('blog_search')
        if user_input:
            blogs = blogs.filter(title__icontains=user_input)

    # Sayfalama işlemi için Paginator kullanımı
    paginator = Paginator(blogs, 6)  # Sayfa başına 6 blog göster
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # Eğer sayfa numarası bir tamsayı değilse, ilk sayfayı göster
        page_obj = paginator.page(1)
    except EmptyPage:
        # Eğer istenen sayfa numarası boşsa, son sayfayı göster
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'title': 'Blog Page',
        'page_obj': page_obj,  # Paginator'un get_page metodu ile sayfaları alıyoruz
        'blog_count': blogs.count(),  
        'user_input': user_input,
    }

    return render(request, 'blog.html', context=context)

# class BlogListView(ListView):
#     model = Blog
#     template_name = 'blog.html'
#     context_object_name = 'blogs'
#     paginate_by = 6  # Sayfa başına gösterilecek blog sayısı

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         user_input = self.request.POST.get('blog_search', '')  # Arama sorgusunu al
#         if user_input:
#             queryset = queryset.filter(title__icontains=user_input)
#         return queryset



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


def shop(request):
    products = Product.objects.filter(is_active=True).order_by("-created_at")
    user_input = ""

     # Arama işlemi POST isteği ile yapılıyorsa
    if request.method == 'POST':
        user_input = request.POST.get('shop_search')
        if user_input:
            products = products.filter(name__icontains=user_input)

    # Sayfalama işlemi için Paginator kullanımı
    paginator = Paginator(products, 6)  # Sayfa başına 6 ürün göster
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # Eğer sayfa numarası bir tamsayı değilse, ilk sayfayı göster
        page_obj = paginator.page(1)
    except EmptyPage:
        # Eğer istenen sayfa numarası boşsa, son sayfayı göster
        page_obj = paginator.page(paginator.num_pages)

    categories = ShopCategory.objects.filter(is_active=True)

    
    context = {
        'title': 'Shop',
        'page_obj': page_obj,  # Paginator'un get_page metodu ile sayfaları alıyoruz
        'products': products,
        'user_input': user_input,
        'categories': categories,
    }
    
    return render(request, 'shop.html', context=context)


def shop_details(request, shop_slug):
    product = Product.objects.get(slug=shop_slug)
    form = None  # Boş bir form tanımlıyoruz

    if request.method == 'POST':
        form = ShopCommentForm(request.POST)
        if form.is_valid():
            form.save()  # Yorumu kaydediyoruz

    context = {
        'title': product.name,
        'product': product,
        'form': form,  # Formu context'e ekliyoruz
    }
    
    return render(request, 'shop-details.html', context=context)

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
  

@login_required
def add_comment(request, shop_slug):
    shop = get_object_or_404(Product, slug=shop_slug)

    if request.method == 'POST':
        form = ShopCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.shop = shop  # Düzeltme: 'blog' değişkeni 'shop' olarak değiştirildi
            comment.save()
            messages.success(request, 'Your comment was successfully added.')
            return redirect('shop_details', shop_slug=shop.slug)  # Düzeltme: 'blog_details' view'i 'shop_details' olarak değiştirildi
    else:
        form = ShopCommentForm()

    return render(request, 'shop-details.html', {'shop': shop, 'form': form})