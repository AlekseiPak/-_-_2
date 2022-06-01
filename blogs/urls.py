from django.urls import path 
from .views import blog_list, book_detail, books_list


urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('books', books_list, name='books_list'),
    path('books/<int:book_id>', book_detail, name='book_detail')
]