from django.urls import path
from . import views

app_name = "gestionapp"

urlpatterns = [
    # Accueil
    path('', views.AccueilView.as_view(), name='accueil'),

    path('admin/', admin.site.urls),
    path('', include('gestionapp.urls', namespace='gestionapp')),

    # Groupes liste des groupes, création, détail, modification et suppression
    path('groups/', views.GroupListView.as_view(), name='group_list'),
    path('groups/create/', views.GroupCreateView.as_view(), name='group_create'),
    path('groups/<int:pk>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('groups/<int:pk>/edit/', views.GroupUpdateView.as_view(), name='group_update'),
    path('groups/<int:pk>/delete/', views.GroupDeleteView.as_view(), name='group_delete'),

    # Étudiants liste des étudiants, création, détail, modification et suppression
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),

    # Enseignants liste des enseignants, création, détail, modification et suppression
    path('teachers/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teachers/create/', views.TeacherCreateView.as_view(), name='teacher_create'),
    path('teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('teachers/<int:pk>/edit/', views.TeacherUpdateView.as_view(), name='teacher_update'),
    path('teachers/<int:pk>/delete/', views.TeacherDeleteView.as_view(), name='teacher_delete'),

    # Cours liste des cours, création, détail, modification et suppression
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/create/', views.CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('courses/<int:pk>/edit/', views.CourseUpdateView.as_view(), name='course_update'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),

    # Absences gestion
    # Liste des absences, création, détail, modification et suppression
    path('absences/', views.AbsenceListView.as_view(), name='absence_list'),
    path('absences/create/', views.AbsenceCreateView.as_view(), name='absence_create'),
    path('absences/<int:pk>/', views.AbsenceDetailView.as_view(), name='absence_detail'),
    path('absences/<int:pk>/edit/', views.AbsenceUpdateView.as_view(), name='absence_update'),
    path('absences/<int:pk>/delete/', views.AbsenceDeleteView.as_view(), name='absence_delete'),

    # Import de fichier d'absences
    path('absences/import/', views.ImportAbsencesView.as_view(), name='import_absences'),

    # Rapports des absences selon le cours ou l'étudiant
    path('reports/course/<int:pk>/', 
         views.CourseAbsencesReportView.as_view(), 
         name='report_course_absences'),
    path('reports/student/<int:pk>/', 
         views.StudentAbsencesReportView.as_view(), 
         name='report_student_absences'),
]