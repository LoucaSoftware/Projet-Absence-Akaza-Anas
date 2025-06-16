from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .models import Group, Student, Teacher, Course, Absence

def index(request):
    return render(request, 'gestionapp/accueil.html')

class AccueilView(TemplateView):
    template_name = 'gestionapp/accueil.html'

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

# Group Detail View
class GroupDetailView(DetailView):
    model = Group
    template_name = 'gestionapp/group/group_detail.html'
    context_object_name = 'group'

# Student Views
class StudentListView(ListView):
    model = Student
    template_name = 'gestionapp/student/student_list.html'
    context_object_name = 'students'

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
    context_object_name = 'student'
    success_url = reverse_lazy('student_list')

# Student Detail View
class StudentDetailView(DetailView):
    model = Student
    template_name = 'gestionapp/student/student_detail.html'
    context_object_name = 'student'

# Teacher Views

# Teacher Detail View
class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'gestionapp/teacher/teacher_detail.html'
    context_object_name = 'teacher'

class TeacherListView(ListView):
    model = Teacher
    template_name = 'gestionapp/teacher/teacher_list.html'
    context_object_name = 'teachers'

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
    context_object_name = 'teacher'
    success_url = reverse_lazy('teacher_list')



# Course Views
class CourseListView(ListView):
    model = Course
    template_name = 'gestionapp/course/course_list.html'
    context_object_name = 'courses'

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
    context_object_name = 'course'
    success_url = reverse_lazy('course_list')

class CourseDetailView(DetailView):
    model = Course
    template_name = 'gestionapp/course/course_detail.html'
    context_object_name = 'course'

# Absence Views
class AbsenceListView(ListView):
    model = Absence
    template_name = 'gestionapp/absence/absence_list.html'
    context_object_name = 'absences'

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
    context_object_name = 'absence'
    success_url = reverse_lazy('absence_list')
class AbsenceDetailView(DetailView):
    model = Absence
    template_name = 'gestionapp/absence/absence_detail.html'
    context_object_name = 'absence'




from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ImportAbsencesForm

class ImportAbsencesView(FormView):
    template_name = 'gestionapp/absence/import_absences.html'
    form_class = ImportAbsencesForm
    success_url = reverse_lazy('absences_list')

    def form_valid(self, form):
        fichier = form.cleaned_data['fichier_csv']
        # TA logique d’import ici…
        return super().form_valid(form)