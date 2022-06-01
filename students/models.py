from django.db import models

class Teacher(models.Model):
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	birth_date = models.DateField()
	school = models.CharField(max_length=150)
	photo = models.ImageField(upload_to= 'teacher_photo', null=True, blank=True)

	def __str__(self):
		return f"{self.name}: {self.subject}"


class Student(models.Model):
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=100)
	birth_date = models.DateField()
	school = models.CharField(max_length=150)
	grade= models.IntegerField()
	average_mark = models.DecimalField(max_digits=2, decimal_places=1)
	photo = models.ImageField(upload_to= 'students_photo', null=True, blank=True)
	teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE, related_name = 'student')

	def __str__(self):
		return f"{self.name}: {self.grade}"