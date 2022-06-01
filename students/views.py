import re
from django.shortcuts import get_object_or_404, redirect, render
from .models import Student, Teacher
from .forms import StudentForm, TeacherForm

def student_list(request,):
	students = Student.objects.all()
	# Берем значение поискового запроса
	search_query = request.GET.get('q', '')
	# ДОбавили 2 поисковик
	grade_query = request.GET.get('grade')
	teachers=Teacher.objects.all()
	if search_query:
		# Если был запрос то сделать фильтрацию.
		students = students.filter(name__contains=search_query)
		# Второй поисковик
	if grade_query:
		students = students.filter(grade=grade_query)

	context = {
		'students': students,
		'search_query': search_query,
		'teachers': teachers
	}

	return render(request, 'students/student_list.html', context)

def student_detail(request, student_id):
	# student = Student.objects.get(id=student_id)
	student = get_object_or_404(Student, id=student_id)
	context = {
		'student': student
	}

	return render(request, 'students/student_detail.html', context)

def	student_create(request):

	form = StudentForm(request.POST or None, files=request.FILES)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('student_list')

	context = {'form': form}
	return render(request, 'students/student_create.html', context)

def student_update(request, student_id):
	student = get_object_or_404(Student, id=student_id)
	form = StudentForm(request.POST or None, instance=student)
	if request.method == 'POST':
		if form.is_valid:
			form.save()
			return redirect('student_list')
	context = {
		'form': form
	}
	return render(request, 'students/student_update.html', context)

def student_delete(request, student_id):
	# Берем ученика из БД
	student = get_object_or_404(Student, id=student_id)
	# Если запрос POST то удаляем и переотправляем на другую страницу
	if request.method == 'POST':
		student.delete()
		return redirect('student_list')
		# В ином случае рисуем страницу для подтверждения
	context = {
		'student': student
	}
	return render(request, 'students/student_delete.html', context)

def teacher_list(request):
	teachers = Teacher.objects.all()
	# Берем значение поискового запроса
	search_query = request.GET.get('q', '')
	# ДОбавили 2 поисковик
	grade_query = request.GET.get('subject')
	if search_query:
		# Если был запрос то сделать фильтрацию.
		teachers = teachers.filter(name__contains=search_query)
	context = {
		'teachers': teachers,
		'search_query': search_query
	}

	return render(request, 'students/teacher_list.html', context)


def teacher_detail(request, teacher_id):
	teacher = get_object_or_404(Teacher, id=teacher_id)
	students = teacher.student.all()
	context = {
		'students': students,
		'teacher': teacher
	}

	return render(request, 'students/teacher_detail.html', context)

def	teacher_create(request):
	form = TeacherForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect(teacher_list)

	context = {'form': form}
	return render(request, 'students/teacher_create.html', context)

def teachers_students(request, teacher_id):
	students = Student.objects.filter(teacher_id=teacher_id)
	teachers = Teacher.objects.all()
	context = {
		'students': students,
		'teachers': teachers
	}

	return render(request, 'students/student_list.html', context)







