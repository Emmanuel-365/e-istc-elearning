from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.views.decorators.http import require_POST
from .decorators import role_required
from .models import User
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.forms import AuthenticationForm
from courses.models import Course
from courses.forms import CourseForm
from evaluations.models import Activite, Soumission, Question, Choix, Tentative
from evaluations.forms import SoumissionForm
import json

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': "Matricule ou Nom d'utilisateur"})
        self.fields['password'].widget.attrs.update({'placeholder': 'Mot de passe'})

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        remember_me = self.request.POST.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0) # Session expire à la fermeture du navigateur
        return super().form_valid(form)

class CustomPasswordResetView(PasswordResetView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['password_reset_confirm_url'] = 'users:password_reset_confirm'
        return context

    def get_success_url(self):
        return reverse_lazy('users:password_reset_done')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    def get_success_url(self):
        return reverse_lazy('users:password_reset_complete')

@login_required
def home(request):
    if request.user.role == User.Role.ETUDIANT:
        return redirect('users:etudiant_dashboard')
    elif request.user.role == User.Role.ENSEIGNANT:
        return redirect('users:enseignant_dashboard')
    elif request.user.is_staff:
        return redirect('/admin/')
    else:
        # Fallback, au cas où
        return redirect('users:login')

@login_required
@role_required(User.Role.ETUDIANT)
def etudiant_dashboard(request):
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'users/dashboard_etudiant.html', {'courses': courses})

@login_required
@role_required(User.Role.ENSEIGNANT)
def enseignant_dashboard(request):
    courses = Course.objects.filter(teacher=request.user).order_by('-created_at')
    return render(request, 'users/dashboard_enseignant.html', {'courses': courses})

# API pour les cours (enseignants)

@login_required
@role_required(User.Role.ENSEIGNANT)
@require_POST
def create_course_teacher(request):
    data = json.loads(request.body)
    data['teacher'] = request.user.id # Assigne l'enseignant connecté
    form = CourseForm(data)
    if form.is_valid():
        course = form.save()
        course_data = {
            'id': course.id,
            'title': course.title,
            'description': course.description,
            'created_at': course.created_at.strftime('%d/%m/%Y')
        }
        return JsonResponse({'status': 'success', 'course': course_data})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@login_required
@role_required(User.Role.ENSEIGNANT)
def course_detail_teacher(request, course_id):
    try:
        course = Course.objects.get(pk=course_id, teacher=request.user)
        data = {
            'id': course.id,
            'title': course.title,
            'description': course.description,
        }
        return JsonResponse(data)
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Cours non trouvé ou vous n\'êtes pas l\'enseignant de ce cours.'}, status=404)

@login_required
@role_required(User.Role.ENSEIGNANT)
@require_POST
def update_course_teacher(request, course_id):
    try:
        course = Course.objects.get(pk=course_id, teacher=request.user)
        data = json.loads(request.body)
        form = CourseForm(data, instance=course)
        if form.is_valid():
            course = form.save()
            course_data = {
                'id': course.id,
                'title': course.title,
                'description': course.description,
                'created_at': course.created_at.strftime('%d/%m/%Y')
            }
            return JsonResponse({'status': 'success', 'course': course_data})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    except Course.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Cours non trouvé ou vous n\'êtes pas l\'enseignant de ce cours.'}, status=404)

@login_required
@role_required(User.Role.ENSEIGNANT)
@require_POST
def delete_course_teacher(request, course_id):
    try:
        course = Course.objects.get(pk=course_id, teacher=request.user)
        course.delete()
        return JsonResponse({'status': 'success'})
    except Course.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Cours non trouvé ou vous n\'êtes pas l\'enseignant de ce cours.'}, status=404)


@login_required
@role_required(User.Role.ETUDIANT)
def student_course_detail(request, course_id):
    from django.core.exceptions import PermissionDenied
    from django.http import Http404
    try:
        course = Course.objects.get(pk=course_id)
        if not request.user.courses.filter(pk=course_id).exists():
            raise PermissionDenied("Vous n'êtes pas inscrit à ce cours.")
        activites = course.activites.all().order_by('due_date')
        # Récupérer les ID des activités déjà soumises par l'étudiant
        submitted_activities_ids = Soumission.objects.filter(
            etudiant=request.user,
            activite__in=activites
        ).values_list('activite_id', flat=True)

        context = {
            'course': course,
            'activites': activites,
            'submitted_activities_ids': submitted_activities_ids
        }
        return render(request, 'users/course_detail_student.html', context)
    except Course.DoesNotExist:
        raise Http404("Cours non trouvé.")
    except PermissionDenied as e:
        return render(request, '403.html', {'message': str(e)}, status=403)

@login_required
@require_POST
def enroll_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        request.user.courses.add(course)
        return JsonResponse({'status': 'success', 'message': 'Inscrit au cours avec succès.'})
    except Course.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Cours non trouvé.'}, status=404)

@login_required
@require_POST
def unenroll_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        request.user.courses.remove(course)
        return JsonResponse({'status': 'success', 'message': 'Désinscrit du cours avec succès.'})
    except Course.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Cours non trouvé.'}, status=404)

@login_required
@role_required(User.Role.ETUDIANT)
def submit_assignment(request, activity_id):
    activite = Activite.objects.get(pk=activity_id)
    # Vérifier si une soumission existe déjà
    if Soumission.objects.filter(activite=activite, etudiant=request.user).exists():
        # On pourrait ajouter un message ici avec le framework de messages de Django
        return redirect('users:student_course_detail', course_id=activite.course.id)

    if request.method == 'POST':
        form = SoumissionForm(request.POST, request.FILES)
        if form.is_valid():
            soumission = form.save(commit=False)
            soumission.activite = activite
            soumission.etudiant = request.user
            soumission.save()
            return redirect('users:student_course_detail', course_id=activite.course.id)
    else:
        form = SoumissionForm()
    return render(request, 'users/submit_assignment.html', {'form': form, 'activite': activite})

@login_required
@role_required(User.Role.ETUDIANT)
def take_quiz(request, activity_id):
    try:
        activite = Activite.objects.get(pk=activity_id, activity_type=Activite.ActivityType.QUIZ)
    except Activite.DoesNotExist:
        raise Http404("Quiz non trouvé.")

    # Vérifier si l'étudiant a déjà soumis ce quiz
    if Tentative.objects.filter(activite=activite, etudiant=request.user).exists():
        # Rediriger vers une page de résultats ou un message indiquant que le quiz a déjà été passé
        return render(request, 'users/quiz_already_taken.html', {'activite': activite})

    questions = activite.questions.all().order_by('id')
    if not questions.exists():
        return render(request, 'users/quiz_no_questions.html', {'activite': activite})

    if request.method == 'POST':
        # Logique de traitement des réponses du quiz
        score = 0
        total_questions = questions.count()

        for question in questions:
            if question.type_question == Question.QuestionType.CHOIX_UNIQUE:
                submitted_choice_id = request.POST.get(f'question_{question.id}')
                correct_choice = question.choix.filter(est_correct=True).first()
                if correct_choice and str(correct_choice.id) == submitted_choice_id:
                    score += 1
            elif question.type_question == Question.QuestionType.CHOIX_MULTIPLE:
                submitted_choices_ids = request.POST.getlist(f'question_{question.id}')
                correct_choices = set(question.choix.filter(est_correct=True).values_list('id', flat=True))
                submitted_choices = set(map(int, submitted_choices_ids))

                if correct_choices == submitted_choices:
                    score += 1
        
        # Enregistrer la tentative
        Tentative.objects.create(
            activite=activite,
            etudiant=request.user,
            score=score
        )
        
        # Rediriger vers une page de résultats ou le tableau de bord
        return render(request, 'users/quiz_results.html', {'activite': activite, 'score': score, 'total_questions': total_questions})

    # Afficher la première question (ou toutes les questions pour un quiz simple)
    return render(request, 'users/take_quiz.html', {'activite': activite, 'questions': questions})

@login_required
@role_required(User.Role.ETUDIANT)
def my_grades(request):
    soumissions = Soumission.objects.filter(etudiant=request.user).order_by('-date_soumission')
    tentatives = Tentative.objects.filter(etudiant=request.user).order_by('-date_tentative')

    context = {
        'soumissions': soumissions,
        'tentatives': tentatives,
    }
    return render(request, 'users/my_grades.html', context)



