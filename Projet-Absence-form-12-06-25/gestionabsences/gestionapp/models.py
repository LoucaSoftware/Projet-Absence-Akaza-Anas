from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)
    number_students = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    def number_students(self):
        return self.students.count()

class Student(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Teacher(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    duration = models.DurationField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return f"{self.title} on {self.date}"

class Absence(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='absences')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='absences')
    justified = models.BooleanField(default=False)
    justification = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"Absence of {self.student} for {self.course} - Justified: {self.justified}"
