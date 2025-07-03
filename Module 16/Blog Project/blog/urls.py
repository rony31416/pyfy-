from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('home/', views.home, name='home'),
    path('new-blog/', views.new_blog, name='add_blog'),
]
