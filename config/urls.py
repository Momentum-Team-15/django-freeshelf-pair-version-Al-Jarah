"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    # path('accounts/logout/', views.logout, name="logout"),
    # path('accounts/login/', views.login, name="login"),
    path('', views.home, name="home"),
    path('resource/<int:pk>/edit/', views.edit, name='edit'),
    path('resource/<int:pk>/delete', views.delete, name='delete'),
    # path('resource/new', views.create_resource, name='create_resource'),
    path('resource/<slug:slug>/', views.resource_detail, name="resource_detail"),
    path('resource/<slug:slug>/', views.category_detail, name="categories_detail"),
    path('favorite/new/<int:res_pk>', views.resource_detail, name="favorite"),
]
