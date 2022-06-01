from django.shortcuts import render
from .models import Blog, Book

def blog_list(request):
	blog = Blog.objects.all() #Запрашиваем базу данных 
	context = {
		'blog': blog
	}
	
	return render(request, 'blogs/blog_list.html', context)

def books_list(request):
	books = Book.objects.all()
	context = {
		'books': books
	}
	return render(request, 'blogs/books_list.html', context)

def book_detail(request, book_id):
	# Получаем одну книгу из БД
	book = Book.objects.get(id = book_id)
	context = {
		'book': book
	}

	return render(request, 'blogs/book_detail.html', context)

