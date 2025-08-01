from django.http import JsonResponse
from django.views.decorators.http import require_POST
from courses.models import Course
from .models import Activite, Question, Choix
from .forms import ActiviteForm, QuestionForm, ChoixForm
from administration.decorators import course_owner_or_admin_required
from .decorators import activity_owner_or_admin_required, question_owner_or_admin_required
import json

@course_owner_or_admin_required
@require_POST
def create_activity(request, course_id):
    course = Course.objects.get(pk=course_id)
    data = json.loads(request.body)
    form = ActiviteForm(data)
    if form.is_valid():
        activite = form.save(commit=False)
        activite.course = course
        activite.save()
        activite_data = {
            'id': activite.id,
            'title': activite.title,
            'description': activite.description,
            'activity_type': activite.get_activity_type_display(),
            'due_date': activite.due_date.isoformat() if activite.due_date else None,
        }
        return JsonResponse({'status': 'success', 'activite': activite_data})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@activity_owner_or_admin_required
def activity_detail(request, activity_id):
    try:
        activite = Activite.objects.get(pk=activity_id)
        data = {
            'id': activite.id,
            'title': activite.title,
            'description': activite.description,
            'activity_type': activite.activity_type,
            'due_date': activite.due_date.isoformat() if activite.due_date else None,
        }
        return JsonResponse(data)
    except Activite.DoesNotExist:
        return JsonResponse({'error': 'Activité non trouvée'}, status=404)

@activity_owner_or_admin_required
@require_POST
def update_activity(request, activity_id):
    try:
        activite = Activite.objects.get(pk=activity_id)
        data = json.loads(request.body)
        form = ActiviteForm(data, instance=activite)
        if form.is_valid():
            activite = form.save()
            activite_data = {
                'id': activite.id,
                'title': activite.title,
                'description': activite.description,
                'activity_type': activite.get_activity_type_display(),
                'due_date': activite.due_date.isoformat() if activite.due_date else None,
            }
            return JsonResponse({'status': 'success', 'activite': activite_data})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    except Activite.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Activité non trouvée'}, status=404)

@activity_owner_or_admin_required
@require_POST
def delete_activity(request, activity_id):
    try:
        activite = Activite.objects.get(pk=activity_id)
        activite.delete()
        return JsonResponse({'status': 'success'})
    except Activite.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Activité non trouvée'}, status=404)

# API pour les questions

@activity_owner_or_admin_required
def list_questions(request, quiz_id):
    questions = Question.objects.filter(activite_id=quiz_id)
    data = {
        'questions': [
            {
                'id': q.id,
                'intitule': q.intitule,
            } for q in questions
        ]
    }
    return JsonResponse(data)

@question_owner_or_admin_required
def question_detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    choix = question.choix.all()
    data = {
        'id': question.id,
        'intitule': question.intitule,
        'type_question': question.type_question,
        'choix': [
            {
                'id': c.id,
                'texte': c.texte,
                'est_correct': c.est_correct
            } for c in choix
        ]
    }
    return JsonResponse(data)

@question_owner_or_admin_required
@require_POST
def create_question(request, quiz_id):
    activite = Activite.objects.get(pk=quiz_id)
    data = json.loads(request.body)
    question = Question.objects.create(
        activite=activite,
        intitule=data['intitule'],
        type_question=data['type_question']
    )
    for choice_data in data['choices']:
        Choix.objects.create(
            question=question,
            texte=choice_data['text'],
            est_correct=choice_data['is_correct']
        )
    return JsonResponse({'status': 'success'})

@question_owner_or_admin_required
@require_POST
def update_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    data = json.loads(request.body)
    question.intitule = data['intitule']
    question.type_question = data['type_question']
    question.save()
    question.choix.all().delete()
    for choice_data in data['choices']:
        Choix.objects.create(
            question=question,
            texte=choice_data['text'],
            est_correct=choice_data['is_correct']
        )
    return JsonResponse({'status': 'success'})

@question_owner_or_admin_required
@require_POST
def delete_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    question.delete()
    return JsonResponse({'status': 'success'})
