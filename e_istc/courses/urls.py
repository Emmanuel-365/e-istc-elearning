from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [     
    # API pour les modules
    path('api/courses/<int:course_id>/modules/create/', views.create_module, name='api_create_module'),
    path('api/modules/<int:module_id>/', views.module_detail, name='api_module_detail'),
    path('api/modules/<int:module_id>/update/', views.update_module, name='api_update_module'),
    path('api/modules/<int:module_id>/delete/', views.delete_module, name='api_delete_module'),

    # API pour les ressources
    path('api/modules/<int:module_id>/ressources/create/', views.create_ressource, name='api_create_ressource'),
    path('api/ressources/<int:ressource_id>/', views.ressource_detail, name='api_ressource_detail'),
    path('api/ressources/<int:ressource_id>/update/', views.update_ressource, name='api_update_ressource'),
    path('api/ressources/<int:ressource_id>/delete/', views.delete_ressource, name='api_delete_ressource'),

    # API pour les étudiants
    path('api/courses/<int:course_id>/students/<int:student_id>/remove/', views.remove_student_from_course, name='api_remove_student_from_course'),
]