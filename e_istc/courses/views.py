from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from users.models import User
from courses.models import Course, Module, Ressource, Annonce
from courses.forms import ModuleForm, RessourceForm, AnnonceForm
from administration.decorators import admin_required, course_owner_or_admin_required, module_owner_or_admin_required, ressource_owner_or_admin_required, annonce_owner_or_admin_required
import json

# API pour les modules

@module_owner_or_admin_required
@require_POST
def create_module(request, course_id):
    """Crée un module pour un cours spécifique.
    """
    course = Course.objects.get(pk=course_id)
    data = json.loads(request.body)
    form = ModuleForm(data)
    if form.is_valid():
        module = form.save(commit=False)
        module.course = course
        module.save()
        module_data = {
            'id': module.id,
            'title': module.title,
            'description': module.description,
            'order': module.order,
        }
        return JsonResponse({'status': 'success', 'module': module_data})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@module_owner_or_admin_required
def module_detail(request, module_id):
    try:
        module = Module.objects.get(pk=module_id)
        data = {
            'id': module.id,
            'title': module.title,
            'description': module.description,
            'order': module.order,
        }
        return JsonResponse(data)
    except Module.DoesNotExist:
        return JsonResponse({'error': 'Module non trouvé'}, status=404)

@module_owner_or_admin_required
@require_POST
def update_module(request, module_id):
    try:
        module = Module.objects.get(pk=module_id)
        data = json.loads(request.body)
        form = ModuleForm(data, instance=module)
        if form.is_valid():
            module = form.save()
            module_data = {
                'id': module.id,
                'title': module.title,
                'description': module.description,
                'order': module.order,
            }
            return JsonResponse({'status': 'success', 'module': module_data})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    except Module.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Module non trouvé'}, status=404)

@module_owner_or_admin_required
@require_POST
def delete_module(request, module_id):
    try:
        module = Module.objects.get(pk=module_id)
        module.delete()
        return JsonResponse({'status': 'success'})
    except Module.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Module non trouvé'}, status=404)

# API pour les ressources

@ressource_owner_or_admin_required
@require_POST
def create_ressource(request, module_id):
    module = Module.objects.get(pk=module_id)
    form = RessourceForm(request.POST, request.FILES)
    if form.is_valid():
        ressource = form.save(commit=False)
        ressource.module = module
        ressource.save()
        ressource_data = {
            'id': ressource.id,
            'title': ressource.title,
            'file_url': ressource.file.url if ressource.file else None,
            'url': ressource.url,
        }
        return JsonResponse({'status': 'success', 'ressource': ressource_data})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@ressource_owner_or_admin_required
def ressource_detail(request, ressource_id):
    try:
        ressource = Ressource.objects.get(pk=ressource_id)
        data = {
            'id': ressource.id,
            'title': ressource.title,
            'file': ressource.file.name if ressource.file else None,
            'url': ressource.url,
        }
        return JsonResponse(data)
    except Ressource.DoesNotExist:
        return JsonResponse({'error': 'Ressource non trouvée'}, status=404)

@ressource_owner_or_admin_required
@require_POST
def update_ressource(request, ressource_id):
    try:
        ressource = Ressource.objects.get(pk=ressource_id)
        form = RessourceForm(request.POST, request.FILES, instance=ressource)
        if form.is_valid():
            ressource = form.save()
            ressource_data = {
                'id': ressource.id,
                'title': ressource.title,
                'file_url': ressource.file.url if ressource.file else None,
                'url': ressource.url,
            }
            return JsonResponse({'status': 'success', 'ressource': ressource_data})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    except Ressource.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Ressource non trouvée'}, status=404)

@ressource_owner_or_admin_required
@require_POST
def delete_ressource(request, ressource_id):
    try:
        ressource = Ressource.objects.get(pk=ressource_id)
        ressource.delete()
        return JsonResponse({'status': 'success'})
    except Ressource.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Ressource non trouvée'}, status=404)

@course_owner_or_admin_required
@require_POST
def remove_student_from_course(request, course_id, student_id):
    try:
        course = Course.objects.get(pk=course_id)
        student = User.objects.get(pk=student_id)
        course.students.remove(student)
        return JsonResponse({'status': 'success'})
    except (Course.DoesNotExist, User.DoesNotExist):
        return JsonResponse({'status': 'error', 'message': 'Cours ou étudiant non trouvé.'}, status=404)

# API pour les annonces

@course_owner_or_admin_required
@require_POST
def create_annonce(request, course_id):
    course = Course.objects.get(pk=course_id)
    data = json.loads(request.body)
    form = AnnonceForm(data)
    if form.is_valid():
        annonce = form.save(commit=False)
        annonce.cours = course
        annonce.save()
        annonce_data = {
            'id': annonce.id,
            'titre': annonce.titre,
            'contenu': annonce.contenu,
            'cree_le': annonce.cree_le.strftime('%d/%m/%Y %H:%M'),
        }
        return JsonResponse({'status': 'success', 'annonce': annonce_data})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@annonce_owner_or_admin_required
def annonce_detail(request, annonce_id):
    try:
        annonce = Annonce.objects.get(pk=annonce_id)
        data = {
            'id': annonce.id,
            'titre': annonce.titre,
            'contenu': annonce.contenu,
        }
        return JsonResponse(data)
    except Annonce.DoesNotExist:
        return JsonResponse({'error': 'Annonce non trouvée'}, status=404)

@annonce_owner_or_admin_required
@require_POST
def update_annonce(request, annonce_id):
    try:
        annonce = Annonce.objects.get(pk=annonce_id)
        data = json.loads(request.body)
        form = AnnonceForm(data, instance=annonce)
        if form.is_valid():
            annonce = form.save()
            annonce_data = {
                'id': annonce.id,
                'titre': annonce.titre,
                'contenu': annonce.contenu,
                'cree_le': annonce.cree_le.strftime('%d/%m/%Y %H:%M'),
            }
            return JsonResponse({'status': 'success', 'annonce': annonce_data})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    except Annonce.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Annonce non trouvée'}, status=404)

@annonce_owner_or_admin_required
@require_POST
def delete_annonce(request, annonce_id):
    try:
        annonce = Annonce.objects.get(pk=annonce_id)
        annonce.delete()
        return JsonResponse({'status': 'success'})
    except Annonce.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Annonce non trouvée'}, status=404)
