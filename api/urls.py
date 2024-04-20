from django.urls import path
from .views import BlogListAPIView, BlogDetailAPIView, BlogCreateAPIView, BlogUpdateAPIView, BlogDeleteAPIView

urlpatterns = [
  path('blogs/', BlogListAPIView.as_view(), name='blog-list'),
  path('blogs/<str:slug>/', BlogDetailAPIView.as_view(), name='blog-detail'),
  path('blogs/create/', BlogCreateAPIView.as_view(), name='blog-create'),
  path('blogs/<str:slug>/update/', BlogUpdateAPIView.as_view(), name='blog-update'),
  path('blogs/<str:slug>/delete', BlogDeleteAPIView.as_view(), name='blog-delete'),

]