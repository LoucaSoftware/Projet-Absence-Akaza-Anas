from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .models import Group, Student, Teacher, Course, Absence
from .forms import CourseForm, StudentForm, TeacherForm, GroupForm, AbsenceForm


# ACCUEIL


class AccueilView(TemplateView):
    template_name = 'gestionapp/accueil.html'

class AccueilView(TemplateView):
    template_name = 'gestionapp/accueil.html'
def group_list(request):
    groups = Group.objects.all()
    return render(request, 'gestionapp/group/group_list.html', {'groups': groups})

def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'gestionapp/group/group_detail.html', {'group': group})

def group_create(request):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestionapp:group_list')
    return render(request, 'gestionapp/group/group_form.html', {'form': form})

def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    form = GroupForm(request.POST or None, instance=group)
    if form.is_valid():
        form.save()
        return redirect('gestionapp:group_list')
    return render(request, 'gestionapp/group/group_form.html', {'form': form})

def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('gestionapp:group_list')
    return render(request, 'gestionapp/group/group_confirm_delete.html', {'group': group})



# STUDENT


def student_list(request):
    students = Student.objects.all()
    return render(request, 'gestionapp/student/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'gestionapp/student/student_detail.html', {'student': student})

def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestionapp:student_list')
    return render(request, 'gestionapp/student/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('gestionapp:student_list')
    return render(request, 'gestionapp/student/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('gestionapp:student_list')
    return render(request, 'gestionapp/student/student_confirm_delete.html', {'student': student})



# TEACHER

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'gestionapp/teacher/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'gestionapp/teacher/teacher_detail.html', {'teacher': teacher})

def teacher_create(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestionapp:teacher_list')
    return render(request, 'gestionapp/teacher/teacher_form.html', {'form': form})

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    form = TeacherForm(request.POST or None, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect('gestionapp:teacher_list')
    return render(request, 'gestionapp/teacher/teacher_form.html', {'form': form})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('gestionapp:teacher_list')
    return render(request, 'gestionapp/teacher/teacher_confirm_delete.html', {'teacher': teacher})



# COURSE

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'gestionapp/course/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'gestionapp/course/course_detail.html', {'course': course})

def course_create(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestionapp:course_list')
    return render(request, 'gestionapp/course/course_form.html', {'form': form})

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('gestionapp:course_list')
    return render(request, 'gestionapp/course/course_form.html', {'form': form})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('gestionapp:course_list')
    return render(request, 'gestionapp/course/course_confirm_delete.html', {'course': course})


# ====================
# ABSENCE
# ====================
def absence_list(request):
    absences = Absence.objects.all()
    return render(request, 'gestionapp/absence/absence_list.html', {'absences': absences})

def absence_detail(request, pk):
    absence = get_object_or_404(Absence, pk=pk)
    return render(request, 'gestionapp/absence/absence_detail.html', {'absence': absence})

def absence_create(request):
    form = AbsenceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestionapp:absence_list')
    return render(request, 'gestionapp/absence/absence_form.html', {'form': form})

def absence_update(request, pk):
    absence = get_object_or_404(Absence, pk=pk)
    form = AbsenceForm(request.POST or None, instance=absence)
    if form.is_valid():
        form.save()
        return redirect('gestionapp:absence_list')
    return render(request, 'gestionapp/absence/absence_form.html', {'form': form})

def absence_delete(request, pk):
    absence = get_object_or_404(Absence, pk=pk)
    if request.method == 'POST':
        absence.delete()
        return redirect('gestionapp:absence_list')
    return render(request, 'gestionapp/absence/absence_confirm_delete.html', {'absence': absence})





from django.views.generic import FormView, ListView
from django.urls import reverse_lazy
from .forms import ImportAbsencesForm
from .models import Absence, Course, Student

class ImportAbsencesView(FormView):
    template_name = 'gestionapp/absence/import_absences.html'
    form_class = ImportAbsencesForm
    success_url = reverse_lazy('gestionapp:absences_list')

    def form_valid(self, form):
        fichier = form.cleaned_data['fichier_csv']
        # TA logique d’import ici…
        return super().form_valid(form)

class CourseAbsencesReportView(ListView):
    model = Absence
    template_name = 'gestionapp/absence/report_course_absences.html'
    context_object_name = 'absences'

    def get_queryset(self):
        course_pk = self.kwargs.get('pk')
        return Absence.objects.filter(course__pk=course_pk)

class StudentAbsencesReportView(ListView):
    model = Absence
    template_name = 'gestionapp/absence/report_student_absences.html'
    context_object_name = 'absences'

    def get_queryset(self):
        student_pk = self.kwargs.get('pk')
        return Absence.objects.filter(student__pk=student_pk)





from .models import Group
from .forms import GroupForm

def group_create(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionapp:group_list')
    else:
        form = GroupForm()
    return render(request, 'gestionapp/group/group_form.html', {'form': form})
