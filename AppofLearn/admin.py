from django.contrib import admin
from .models import Board,Book,Genre,Author,BookInstance,Topic,Board,Post
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Board)