from django.urls import path
from .views import student_list, student_detail, student_create, teacher_create, teacher_list, teacher_detail, student_update, student_delete, teachers_students

urlpatterns = [
	path('students', student_list, name='student_list'),
	path('student/update/<int:student_id>', student_update, name='student_update'),
	path('student_create', student_create, name='student_create'),
	path('student/<int:student_id>', student_detail, name='student_detail'),
	path('teachers', teacher_list, name='teacher_list'),
	path('teacher_create', teacher_create, name='teacher_create'),
	path('teacher/<int:teacher_id>', teacher_detail, name='teacher_detail'),
	path('student/delete/<int:student_id>', student_delete, name='student_delete'),
	path('teachers/students/<int:teacher_id>', teachers_students, name='teachers_students')
]
	
