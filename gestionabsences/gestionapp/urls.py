from django.urls import path, include
from django.contrib import admin
from . import views

app_name = "gestionapp"

urlpatterns = [
    # Accueil
    path('', views.AccueilView.as_view(), name='accueil'),

    path('admin/', admin.site.urls),
    # Removed recursive include to prevent infinite recursion
    # path('', include(('gestionapp.urls', 'gestionapp'), namespace='gestionapp')),

    # GROUPS
    path('groups/', views.group_list, name='group_list'),
    path('groups/create/', views.group_create, name='group_create'),
    path('groups/<int:pk>/', views.group_detail, name='group_detail'),
    path('groups/edit/<int:pk>/', views.group_update, name='group_update'),
    path('groups/delete/<int:pk>/', views.group_delete, name='group_delete'),

    # STUDENTS
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/edit/<int:pk>/', views.student_update, name='student_update'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),

    # TEACHERS

     path('teachers/', views.teacher_list, name='teacher_list'),
     path('teachers/create/', views.teacher_create, name='teacher_create'),
     path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
     path('teachers/edit/<int:pk>/', views.teacher_update, name='teacher_update'),
     path('teachers/delete/<int:pk>/', views.teacher_delete, name='teacher_delete'),

     # COURSES
     path('courses/', views.course_list, name='course_list'),
     path('courses/create/', views.course_create, name='course_create'),
     path('courses/<int:pk>/', views.course_detail, name='course_detail'),
     path('courses/edit/<int:pk>/', views.course_update, name='course_update'),
     path('courses/delete/<int:pk>/', views.course_delete, name='course_delete'),

    
    # ABSENCES
     path('absences/', views.absence_list, name='absence_list'),
     path('absences/create/', views.absence_create, name='absence_create'),
     path('absences/<int:pk>/', views.absence_detail, name='absence_detail'),
     path('absences/edit/<int:pk>/', views.absence_update, name='absence_update'),
     path('absences/delete/<int:pk>/', views.absence_delete, name='absence_delete'),

    # IMPORT FICHIER D’ABSENCES
    path('absences/import/', views.ImportAbsencesView.as_view(), name='import_absences'),

    # RAPPORTS SELON LE COURS OU STUDENT
    path('reports/course/<int:pk>/', 
         views.CourseAbsencesReportView.as_view(), 
         name='report_course_absences'),
    path('reports/student/<int:pk>/', 
         views.StudentAbsencesReportView.as_view(), 
         name='report_student_absences'),
]