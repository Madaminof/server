from django.views.generic import ListView,DetailView,UpdateView
from django.shortcuts import render
from .models import *
# Create your views here.


class BookView(ListView):
    model=Book
    template_name='book/book_list.html'
    context_object_name = 'book'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'


class Savat(BookDetailView):
    model=Book
    template_name='book/savat.html'

class BookUpdateView(UpdateView):
    model=Book
    fields=['price']
    template_name='book/book_update.html'

