from django.views.generic import ListView  
from django.shortcuts import redirect, render
from django.http import HttpResponse
from core.forms import CommentForm, ContactForm
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
  product = Product.objects.get(slug = shop_slug)

  context = {
    'title' : product.name,
    'product' : product,
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
  

def shop_add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page, or render a success message
            return redirect('success_url_name')
    else:
        form = CommentForm()
    
    return render(request, 'shop-details.html', {'form': form})


