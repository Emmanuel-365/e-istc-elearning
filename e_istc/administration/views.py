from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from users.models import User
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from courses.models import Course, Module, Ressource
from courses.forms import CourseForm, ModuleForm, RessourceForm
from evaluations.models import Activite
from .decorators import admin_required, course_owner_or_admin_required
import json

@admin_required
def user_management_page(request):
    users = User.objects.all().order_by('last_name')
    return render(request, 'administration/user_management.html', {'users': users})

@admin_required
def course_management_page(request):
    courses = Course.objects.all().order_by('-created_at')
    teachers = User.objects.filter(role=User.Role.ENSEIGNANT)
    return render(request, 'administration/course_management.html', {'courses': courses, 'teachers': teachers})

@course_owner_or_admin_required
def course_detail_page(request, course_id):
    course = Course.objects.get(pk=course_id)
    enrolled_students = course.students.all()
    activites = course.activites.all().order_by('-created_at')
    context = {
        'course': course,
        'enrolled_students': enrolled_students,
        'activites': activites,
    }
    return render(request, 'administration/course_detail_page.html', context)

@admin_required
@require_POST
def create_user(request):
    data = json.loads(request.body)
    form = CustomUserCreationForm(data)
    if form.is_valid():
        user = form.save()
        user_data = {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'role': user.role,
            'get_role_display': user.get_role_display(),
            'matricule': user.matricule,
            'specialite': user.specialite,
        }
        return JsonResponse({'status': 'success', 'user': user_data})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@admin_required
def user_detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        data = {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'role': user.role,
            'matricule': user.matricule,
            'specialite': user.specialite,
        }
        return JsonResponse(data)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Utilisateur non trouvé'}, status=404)

@admin_required
@require_POST
def update_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        data = json.loads(request.body)
        form = CustomUserChangeForm(data, instance=user)
        if form.is_valid():
            user = form.save()
            user_data = {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'role': user.role,
                'get_role_display': user.get_role_display(),
                'matricule': user.matricule,
                'specialite': user.specialite,
            }
            return JsonResponse({'status': 'success', 'user': user_data})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    except User.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Utilisateur non trouvé'}, status=404)


# API pour les cours

@admin_required
@require_POST
def create_course(request):
    data = json.loads(request.body)
    # Si l'utilisateur est un enseignant, attribuer le cours à lui-même
    if request.user.role == User.Role.ENSEIGNANT:
        data['teacher'] = request.user.id
    form = CourseForm(data)
    if form.is_valid():
        course = form.save()
        course_data = {
            'id': course.id,
            'title': course.title,
            'teacher': {
                'id': course.teacher.id,
                'name': f'{course.teacher.first_name} {course.teacher.last_name}'
            },
            'created_at': course.created_at.strftime('%d/%m/%Y')
        }
        return JsonResponse({'status': 'success', 'course': course_data})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@admin_required
def course_detail(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        data = {
            'id': course.id,
            'title': course.title,
            'description': course.description,
            'teacher_id': course.teacher.id
        }
        return JsonResponse(data)
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Cours non trouvé'}, status=404)

@admin_required
@require_POST
def update_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        data = json.loads(request.body)
        form = CourseForm(data, instance=course)
        if form.is_valid():
            course = form.save()
            course_data = {
                'id': course.id,
                'title': course.title,
                'teacher': {
                    'id': course.teacher.id,
                    'name': f'{course.teacher.first_name} {course.teacher.last_name}'
                },
                'created_at': course.created_at.strftime('%d/%m/%Y')
            }
            return JsonResponse({'status': 'success', 'course': course_data})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    except Course.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Cours non trouvé'}, status=404)

@admin_required
@require_POST
def delete_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        course.delete()
        return JsonResponse({'status': 'success'})
    except Course.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Cours non trouvé'}, status=404)

@admin_required
@require_POST
def delete_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        user.delete()
        return JsonResponse({'status': 'success'})
    except User.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Utilisateur non trouvé'}, status=404)

