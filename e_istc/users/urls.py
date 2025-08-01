from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/etudiant/', views.etudiant_dashboard, name='etudiant_dashboard'),
    path('dashboard/enseignant/', views.enseignant_dashboard, name='enseignant_dashboard'),
    path('courses/<int:course_id>/', views.student_course_detail, name='student_course_detail'),
    path('activity/<int:activity_id>/submit/', views.submit_assignment, name='submit_assignment'),
    path('password_reset/', views.CustomPasswordResetView.as_view(template_name='users/registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(template_name='users/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/registration/password_reset_complete.html'), name='password_reset_complete'),
    path('api/courses/<int:course_id>/enroll/', views.enroll_course, name='api_enroll_course'),
    path('api/courses/<int:course_id>/unenroll/', views.unenroll_course, name='api_unenroll_course'),

    # API pour les cours (enseignants)
    path('api/teacher/courses/create/', views.create_course_teacher, name='api_create_course_teacher'),
    path('api/teacher/courses/<int:course_id>/', views.course_detail_teacher, name='api_course_detail_teacher'),
    path('api/teacher/courses/<int:course_id>/update/', views.update_course_teacher, name='api_update_course_teacher'),
    path('api/teacher/courses/<int:course_id>/delete/', views.delete_course_teacher, name='api_delete_course_teacher'),
]
