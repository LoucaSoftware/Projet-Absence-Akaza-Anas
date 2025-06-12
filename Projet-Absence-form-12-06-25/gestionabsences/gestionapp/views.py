from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Group, Student, Teacher, Course, Absence

def index(request):
    return render(request, 'gestionapp/index.html')

# Group Views
class GroupListView(ListView):
    model = Group
    template_name = 'gestionapp/group/group_list.html'
    context_object_name = 'groups'

class GroupCreateView(CreateView):
    model = Group
    fields = ['name']
    template_name = 'gestionapp/group/group_form.html'
    success_url = reverse_lazy('group_list')

class GroupUpdateView(UpdateView):
    model = Group
    fields = ['name']
    template_name = 'gestionapp/group/group_form.html'
    success_url = reverse_lazy('group_list')

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'gestionapp/group/group_confirm_delete.html'
    success_url = reverse_lazy('group_list')

# Student Views
class StudentListView(ListView):
    model = Student
    template_name = 'gestionapp/student/student_list.html'

class StudentCreateView(CreateView):
    model = Student
    fields = ['last_name', 'first_name', 'group']
    template_name = 'gestionapp/student/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['last_name', 'first_name', 'group']
    template_name = 'gestionapp/student/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'gestionapp/student/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

# Teacher Views
class TeacherListView(ListView):
    model = Teacher
    template_name = 'gestionapp/teacher/teacher_list.html'

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['last_name', 'first_name']
    template_name = 'gestionapp/teacher/teacher_form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['last_name', 'first_name']
    template_name = 'gestionapp/teacher/teacher_form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'gestionapp/teacher/teacher_confirm_delete.html'
    success_url = reverse_lazy('teacher_list')

# Course Views
class CourseListView(ListView):
    model = Course
    template_name = 'gestionapp/course/course_list.html'

class CourseCreateView(CreateView):
    model = Course
    fields = ['title', 'date', 'teacher', 'duration', 'group']
    template_name = 'gestionapp/course/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    fields = ['title', 'date', 'teacher', 'duration', 'group']
    template_name = 'gestionapp/course/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'gestionapp/course/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')

# Absence Views
class AbsenceListView(ListView):
    model = Absence
    template_name = 'gestionapp/absence/absence_list.html'

class AbsenceCreateView(CreateView):
    model = Absence
    fields = ['student', 'course', 'justified', 'justification']
    template_name = 'gestionapp/absence/absence_form.html'
    success_url = reverse_lazy('absence_list')

class AbsenceUpdateView(UpdateView):
    model = Absence
    fields = ['student', 'course', 'justified', 'justification']
    template_name = 'gestionapp/absence/absence_form.html'
    success_url = reverse_lazy('absence_list')

class AbsenceDeleteView(DeleteView):
    model = Absence
    template_name = 'gestionapp/absence/absence_confirm_delete.html'
    success_url = reverse_lazy('absence_list')

