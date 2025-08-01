from django.urls import path
from . import views

app_name = 'evaluations'

urlpatterns = [
    path('api/courses/<int:course_id>/activities/create/', views.create_activity, name='api_create_activity'),
    path('api/activities/<int:activity_id>/', views.activity_detail, name='api_activity_detail'),
    path('api/activities/<int:activity_id>/update/', views.update_activity, name='api_update_activity'),
    path('api/activities/<int:activity_id>/delete/', views.delete_activity, name='api_delete_activity'),
]
