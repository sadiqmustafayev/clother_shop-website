from django.urls import path
from core.views import (
  index,
  about,
  blog_details,
  blog,
  checkout,
  contact_us,
  shop_details,
  shop,
  shopping_cart
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
]
