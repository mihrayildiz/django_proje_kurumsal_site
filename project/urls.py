"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('references/', views.references, name='references'),
    path('contactus/', views.contactus, name='contactus'),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('menu/', include('menu.urls')),
    path('announcement/', include('announcement.urls')),
    path('category/<int:id>/<slug:slug>/', views.category_products, name ='category_products'),
    path('announcement/<int:id>/<slug:slug>/', views.announcement_detail, name='announcement_detail'),
    path('search/', views.announcement_search, name='announcement_search'),
    path('search_auto/', views.announcement_search_auto, name='announcement_search_auto'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('join/', views.join_view, name='join_view'),
    path('user/', include('user.urls')),
    path('faq/', views.faq, name='faq'),
    path('menu/<int:id>', views.menu, name='menu'),
    path('menu/<int:id>/<slug:slug>', views.content_detail, name='content_detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),





]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
