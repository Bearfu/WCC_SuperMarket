"""WCC_SuperMarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.Table, name='Home'),
    url(r'^table', views.Table, name='table'),
    url(r'^test', views.Test, name='test'),
    url(r'^add$', views.add_products, name='add_products'),
    url(r'api/test$', views.Test, name='test'),
    url(r'api/purchase/upload_index$', views.upload_index, name='upload_index'),
    url(r'api/purchase/get_product_info$', views.get_product_info, name='get_product_info'),
    url(r'api/purchase/order_list$', views.order_list, name='order_list'),
    url(r'api/purchase/Write_off$', views.Write_off, name='Write_off'),
    url(r'api/purchase/print_rainbowcode$', views.print_rainbowcode, name='print_rainbowcode'),



]
