# from pyexpat.errors import messages
from django.contrib import messages
from django.views.generic import ListView  
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.forms import BlogCommentForm, ShopCommentForm, ContactForm
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
    sizes = Size.objects.all()
    colors = Color.objects.all()

    # Fiyat aralıkları listesi
    price_ranges = [
        {"start": 0, "end": 50},
        {"start": 50, "end": 100},
        {"start": 100, "end": 150},
        # Diğer fiyat aralıkları buraya eklenebilir
    ]

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Her fiyat aralığı için ürün sayısını hesapla
    def count_products_in_price_range(min_price, max_price):
        return Product.objects.filter(price__gte=min_price, price__lte=max_price).count()

    product_counts = {f"{price_range['start']}-{price_range['end']}": count_products_in_price_range(price_range["start"], price_range["end"]) for price_range in price_ranges}

    context = {
        'title': 'Shop',
        'page_obj': page_obj,  # Paginator'un get_page metodu ile sayfaları alıyoruz
        'products': products,
        'user_input': user_input,
        'categories': categories,
        'sizes': sizes,
        'colors': colors,
        'min_price': min_price,
        'max_price': max_price,
        'price_ranges': price_ranges,
        'product_counts': product_counts,
    }

    return render(request, 'shop.html', context=context)


def shop_details(request, shop_slug):
    product = Product.objects.get(slug=shop_slug)
    form = None  # Boş bir form tanımlıyoruz
    sizes = Size.objects.filter(product=product)
    


    if request.method == 'POST':
        form = ShopCommentForm(request.POST)
        if form.is_valid():
            form.save()  # Yorumu kaydediyoruz

    context = {
        'title': product.name,
        'product': product,
        'form': form,  # Formu context'e ekliyoruz
        'sizes': sizes,
    }
    
    return render(request, 'shop-details.html', context=context)



@login_required
def add_comment(request, shop_slug):
    shop = get_object_or_404(Product, slug=shop_slug)

    if request.method == 'POST':
        form = ShopCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.shop = shop
            comment.product_id = shop.id 
            comment.save()
            messages.success(request, 'Your comment was successfully added.')
            return redirect('shop_details', shop_slug=shop_slug)
    else:
        form = ShopCommentForm()

    context = {
        'title': shop.name,
        'shop': shop,
        'form': form,
    }
    
    return render(request, 'shop-details.html', context=context)

@login_required
def blog_add_comment(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)

    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            # Yorum başarıyla eklendiğinde yönlendirme yapabilirsiniz
            return redirect('blog-details', blog_slug=blog.slug)
    else:
        form = BlogCommentForm()

    context = {
        'title': blog.title,
        'blog': blog,
        'form': form,
    }

    return render(request, 'blog-details.html', context=context)


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
  

def filter_price(request):
    # Fiyat aralıklarını belirleyin, bu örnekte varsayılan fiyat aralıkları kullanılıyor
    price_ranges = [
        {"start": 0.00, "end": 50.00},
        {"start": 50.00, "end": 100.00},
        {"start": 100.00, "end": 150.00},
        {"start": 150.00, "end": 200.00},
        {"start": 200.00, "end": 250.00},
        {"start": 250.00, "end": None},  # None, 250.00+ için sonsuz olarak kabul edilir
    ]

    return render(request, 'filter_price.html', {'price_ranges': price_ranges})