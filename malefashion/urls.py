"""
URL configuration for clothershop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# from django.urls.conf import include 
from core.urls import urlpatterns as core_urls
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from user.urls import urlpatterns as user_urlpatterns





urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include(core_urls)),
]

urlpatterns += i18n_patterns(
  path('admin/', admin.site.urls),
  path('', include(core_urls)),
  path('user/', include(user_urlpatterns)),
  path('i18n/', include('django.conf.urls.i18n')),
)


if 'rosetta' in settings.INSTALLED_APPS:
  urlpatterns += [re_path('translate/', include('rosetta.urls')) ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
