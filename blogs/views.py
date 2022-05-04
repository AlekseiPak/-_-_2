from django.shortcuts import render
from .models import Blog
def blog_list(request):
	blog = Blog.objects.first() #Запрашиваем базу данных 
	context = {
		'blog': blog
	}
	
	return render(request, 'blogs/blog_list.html', context)

