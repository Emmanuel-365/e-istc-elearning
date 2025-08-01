from django.core.exceptions import PermissionDenied
from users.models import User
from .models import Activite, Question

def activity_owner_or_admin_required(view_func):
    """
    Decorator for views that checks that the user is logged in and is either an admin
    or the teacher of the activity's course.
    It assumes that the view kwargs contain 'activity_id'.
    """
    def wrapper(request, *args, **kwargs):
        activity_id = kwargs.get('activity_id') or kwargs.get('quiz_id')
        if not activity_id:
            raise PermissionDenied

        try:
            # Get the activity and the related course teacher in one query
            activity = Activite.objects.select_related('course__teacher').get(pk=activity_id)
            course_teacher = activity.course.teacher
        except Activite.DoesNotExist:
            # Return a 404-like response if activity does not exist
            raise PermissionDenied

        user = request.user
        if not user.is_authenticated:
            raise PermissionDenied

        # Check if the user is an admin or the teacher of the course
        if user.role == User.Role.ADMIN or user == course_teacher:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrapper

def question_owner_or_admin_required(view_func):
    """
    Decorator for views that checks that the user is logged in and is either an admin
    or the teacher of the question's activity's course.
    It assumes that the view kwargs contain 'question_id'.
    """
    def wrapper(request, *args, **kwargs):
        question_id = kwargs.get('question_id')
        if not question_id:
            raise PermissionDenied

        try:
            question = Question.objects.select_related('activite__course__teacher').get(pk=question_id)
            course_teacher = question.activite.course.teacher
        except Question.DoesNotExist:
            raise PermissionDenied

        user = request.user
        if not user.is_authenticated:
            raise PermissionDenied

        if user.role == User.Role.ADMIN or user == course_teacher:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrapper
