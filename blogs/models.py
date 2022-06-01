from django.db import models

# def book_cover_directory(instance, filename):
# 	return f"{settings.MEDIA_ROOT}/covers/{instance.title}/{filename}"

class Blog(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	creation_date = models.DateField()

	def __str__(self):
		return self.title

class Book(models.Model):
	title = models.CharField(max_length=200, unique=True)
	description = models.TextField(null=False)
	release_date = models.DateField(auto_now_add=True)
	number_of_pages = models.PositiveIntegerField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=6)
	in_stock = models.BooleanField(default=True)
	cover = models.ImageField(upload_to= 'covers')

	def __str__(self):
		return self.title

		
		