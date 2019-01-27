from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from .models import Board,Book, Author, BookInstance, Genre
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
def home(request):
    boards = Board.objects.all()
    boards_names = list()
    for board in boards:
        boards_names.append(board.name)
    response_html = '<br>'.join(boards_names)
    return HttpResponse(response_html)

class books(ListView):
    model = Book
    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Book.objects.all()
    template_name = 'my_arbitrary_template_name_list.html'  # Specify your own template name/location
class BookDetailView(DetailView):
    model = Book
    template_name='book_detail.html'

class AuthorCreate(CreateView):
    model = User
    fields = '__all__'
    template_name='author_form.html'
class AuthorUpdate(UpdateView):
    model = User
    fields = '__all__'
    template_name='author_form.html'

class AuthorDelete(DeleteView):
    model = User
    template_name='author_form.html'
    success_url = reverse_lazy('books')

