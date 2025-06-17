from django import forms
from .models import Group, Student, Teacher, Course, Absence


# ===== GROUP =====
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


# ===== STUDENT =====
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'group']


# ===== TEACHER =====
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email']


# ===== COURSE =====
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'teacher', 'group', 'start_date', 'end_date']


# ===== ABSENCE =====
class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['student', 'course', 'date', 'reason']


# ===== IMPORT CSV D’ABSENCES =====
class ImportAbsencesForm(forms.Form):
    fichier_csv = forms.FileField(
        label="Fichier CSV d'absences",
        help_text="Importe un fichier CSV contenant les absences."
    )