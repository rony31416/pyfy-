from django.urls import path 
from . import views 

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),  # <--- add name here
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
