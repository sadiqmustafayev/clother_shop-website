from django.urls import include
from django.urls import path
from django.views.i18n import set_language
from core.views import (
  index,
  about,
  blog_details,
  blog,
  checkout,
  contact_us,
  shop_details,
  shop,
  shopping_cart,
  faq,
)

urlpatterns = [
    path('', index, name='home'), 
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog-details/<str:blog_slug>/', blog_details, name='blog-details'),
    # path('blog-details/<int:blog_id>', blog_details, name='blog_details'),
    path('checkout/', checkout, name='checkout'),
    path('contact-us/', contact_us, name='contact_us'),
    path('shop-details/', shop_details, name='shop_details'),
    path('shop/', shop, name='shop'),
    path('shopping-cart/', shopping_cart, name='shopping_cart'),
    path('faq/', faq, name='faq'),
    path('set-language/', set_language, name='set_language'),
    path('', include('social_django.urls', namespace='social')),
]
