# from django.shortcuts import render
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Helo, This is book management app");


from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book_list.html'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')