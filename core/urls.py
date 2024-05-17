from core import views
from django.urls import include
from django.urls import path 
from django.views.i18n import set_language
from core.views import (
  
  blog_add_comment,
  index,
  about,
  blog_details,
  blog,
  checkout,
  contact_us,
  shop_details,
  shop,
  add_comment,
  shopping_cart,
  faq,
)

urlpatterns = [
    path('', index, name='home'), 
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    # path('blog/', BlogListView.as_view(), name='blog'),
    path('blog-details/<str:blog_slug>/', blog_details, name='blog-details'),
    # path('blog-details/<int:blog_id>', blog_details, name='blog_details'),
    path('checkout/', checkout, name='checkout'),
    path('contact-us/', contact_us, name='contact_us'),
    # path('shop-details/', shop_details, name='shop_details'),
    path('shop/', shop, name='shop'),
    path('shop-details/<str:shop_slug>/', shop_details, name='shop_details'),
    path('shopping-cart/', shopping_cart, name='shopping_cart'),
    path('faq/', faq, name='faq'),
    path('set-language/', set_language, name='set_language'),
    # path('comment_submit/<slug:slug>/', add_comment, name='comment_submit'),
    # path('add_comment/<slug:shop_slug>/', add_comment, name='add_comment'),
    # path('shop-details/add_comment/<slug:shop_slug>/', add_comment, name='add_comment'),
    path('shop-details/<str:shop_slug>/add_comment/', add_comment, name='add_comment'),
    path('blog-details/<str:blog_slug>/add_comment/', blog_add_comment, name='blog_add_comment'),
    path('send_email/', views.send_email, name='send_email'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('', include('social_django.urls', namespace='social')),
]
