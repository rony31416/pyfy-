from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('home/', views.home, name='home'),
    path('new-blog/', views.new_blog, name='add_blog'),
    path('edit-blog/<int:pk>/', views.edit_blog, name='edit_blog'),
    path('delete-blog/<int:pk>/', views.delete_blog, name='delete_blog'),
]