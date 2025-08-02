from django.test import TestCase, Client
from django.urls import reverse
from users.models import User
from courses.models import Course
import json

class AdministrationAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_user(username='admin', email='admin@example.com', password='password', role=User.Role.ADMIN, is_staff=True, is_superuser=True)
        self.teacher_user = User.objects.create_user(username='teacher', email='teacher@example.com', password='password', role=User.Role.ENSEIGNANT)
        self.student_user = User.objects.create_user(username='student', email='student@example.com', password='password', role=User.Role.ETUDIANT)

    # User Management API Tests
    def test_create_user_api_admin(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(reverse('administration:api_create_user'),
                                    json.dumps({'username': 'newuser', 'email': 'new@example.com', 'first_name': 'New', 'last_name': 'User', 'role': User.Role.ETUDIANT, 'matricule': 'NEW001'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 4)

    def test_create_user_api_non_admin(self):
        self.client.login(username='teacher', password='password')
        response = self.client.post(reverse('administration:api_create_user'),
                                    json.dumps({'username': 'unauthuser', 'email': 'unauth@example.com', 'role': User.Role.ETUDIANT}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 403) # Forbidden

    def test_user_detail_api_admin(self):
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('administration:api_user_detail', args=[self.student_user.id]))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['email'], 'student@example.com')

    def test_user_detail_api_non_admin(self):
        self.client.login(username='teacher', password='password')
        response = self.client.get(reverse('administration:api_user_detail', args=[self.student_user.id]))
        self.assertEqual(response.status_code, 403) # Forbidden

    def test_update_user_api_admin(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(reverse('administration:api_update_user', args=[self.student_user.id]),
                                    json.dumps({'username': 'updatedstudent', 'email': 'updated@example.com', 'first_name': 'Updated', 'last_name': 'Student', 'role': User.Role.ETUDIANT, 'matricule': 'UPD001', 'specialite': '', 'is_active': True}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.student_user.refresh_from_db()
        self.assertEqual(self.student_user.email, 'updated@example.com')

    def test_update_user_api_non_admin(self):
        self.client.login(username='teacher', password='password')
        response = self.client.post(reverse('administration:api_update_user', args=[self.student_user.id]),
                                    json.dumps({'username': 'updatedstudent', 'email': 'updated@example.com', 'first_name': 'Updated', 'last_name': 'Student', 'role': User.Role.ETUDIANT, 'matricule': 'UPD001', 'specialite': '', 'is_active': True}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 403) # Forbidden

    def test_delete_user_api_admin(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(reverse('administration:api_delete_user', args=[self.student_user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 2) # 3 initial - 1 deleted

    def test_delete_user_api_non_admin(self):
        self.client.login(username='teacher', password='password')
        response = self.client.post(reverse('administration:api_delete_user', args=[self.student_user.id]))
        self.assertEqual(response.status_code, 403) # Forbidden

    # Course Management API Tests
    def test_create_course_api_admin(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(reverse('administration:api_create_course'),
                                    json.dumps({'title': 'New Course', 'description': 'Desc', 'teacher': self.teacher_user.id}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Course.objects.count(), 1)

    def test_create_course_api_non_admin(self):
        self.client.login(username='teacher', password='password')
        response = self.client.post(reverse('administration:api_create_course'),
                                    json.dumps({'title': 'New Course', 'description': 'Desc', 'teacher': self.teacher_user.id}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 403) # Forbidden

    def test_course_detail_api_admin(self):
        course = Course.objects.create(title='Detail Course', description='Desc', teacher=self.teacher_user)
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('administration:api_course_detail', args=[course.id]))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['title'], 'Detail Course')

    def test_course_detail_api_non_admin(self):
        course = Course.objects.create(title='Detail Course', description='Desc', teacher=self.teacher_user)
        self.client.login(username='teacher', password='password')
        response = self.client.get(reverse('administration:api_course_detail', args=[course.id]))
        self.assertEqual(response.status_code, 403) # Forbidden

    def test_update_course_api_admin(self):
        course = Course.objects.create(title='Update Course', description='Desc', teacher=self.teacher_user)
        self.client.login(username='admin', password='password')
        response = self.client.post(reverse('administration:api_update_course', args=[course.id]),
                                    json.dumps({'title': 'Updated Course', 'description': 'Updated Desc', 'teacher': self.teacher_user.id}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        course.refresh_from_db()
        self.assertEqual(course.title, 'Updated Course')

    def test_update_course_api_non_admin(self):
        course = Course.objects.create(title='Update Course', description='Desc', teacher=self.teacher_user)
        self.client.login(username='teacher', password='password')
        response = self.client.post(reverse('administration:api_update_course', args=[course.id]),
                                    json.dumps({'title': 'Updated Course', 'description': 'Updated Desc', 'teacher': self.teacher_user.id}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 403) # Forbidden

    def test_delete_course_api_admin(self):
        course = Course.objects.create(title='Delete Course', description='Desc', teacher=self.teacher_user)
        self.client.login(username='admin', password='password')
        response = self.client.post(reverse('administration:api_delete_course', args=[course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Course.objects.count(), 0)

    def test_delete_course_api_non_admin(self):
        course = Course.objects.create(title='Delete Course', description='Desc', teacher=self.teacher_user)
        self.client.login(username='teacher', password='password')
        response = self.client.post(reverse('administration:api_delete_course', args=[course.id]))
        self.assertEqual(response.status_code, 403) # Forbidden
