from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)
    number_students = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='courses')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='courses')
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.DurationField()

    def __str__(self):
        return self.name


class Absence(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='absences')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='absences')
    date = models.DateField()
    reason = models.CharField(max_length=255, blank=True, null=True)
    justified = models.BooleanField(default=False)
    justification = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.course} ({self.date})"