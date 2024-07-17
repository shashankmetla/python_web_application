from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import DoctorSignUpForm, PatientSignUpForm
from .views import DoctorSignUpView, PatientSignUpView, SignUpView


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="vivek",
            first_name="Vivek",
            last_name="Singh",
            email="vivek@gmail.com",
            password="pass12345",
            line="adderess line",
            city="user city",
            state="user state",
            pincode=226006,
        )
        self.assertEqual(user.username, "vivek")
        self.assertEqual(user.first_name, "Vivek")
        self.assertEqual(user.last_name, "Singh")
        self.assertEqual(user.email, "vivek@gmail.com")
        self.assertEqual(user.line, "adderess line")
        self.assertEqual(user.city, "user city")
        self.assertEqual(user.state, "user state")
        self.assertEqual(user.pincode, 226006)
        self.assertFalse(user.is_doctor)
        self.assertFalse(user.is_patient)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="supervivek",
            first_name="Vivek",
            last_name="Singh",
            email="viveksuper@gmail.com",
            password="pass12345",
            line="adderess line",
            city="superuser city",
            state="superuser state",
            pincode=226006,
        )
        self.assertEqual(admin_user.username, "supervivek")
        self.assertEqual(admin_user.email, "viveksuper@gmail.com")
        self.assertEqual(admin_user.first_name, "Vivek")
        self.assertEqual(admin_user.last_name, "Singh")
        self.assertEqual(admin_user.line, "adderess line")
        self.assertEqual(admin_user.city, "superuser city")
        self.assertEqual(admin_user.state, "superuser state")
        self.assertEqual(admin_user.pincode, 226006)
        self.assertFalse(admin_user.is_doctor)
        self.assertFalse(admin_user.is_patient)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_active)


class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")


class SignupPageTest(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")

    def test_signup_view(self):
        view = resolve("/signup/")
        self.assertEqual(view.func.__name__, SignUpView.as_view().__name__)


class DoctorSignUpTest(TestCase):
    def setUp(self):
        url = reverse("signup_doctor")
        self.response = self.client.get(url)

    def test_doctor_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup_form.html")

    def test_doctor_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, DoctorSignUpForm)

    def test_doctor_signup_view(self):
        view = resolve("/signup/doctor/")
        self.assertEqual(view.func.__name__, DoctorSignUpView.as_view().__name__)


class PatientSignUpTest(TestCase):
    def setUp(self):
        url = reverse("signup_patient")
        self.response = self.client.get(url)

    def test_doctor_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup_form.html")

    def test_doctor_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, PatientSignUpForm)

    def test_doctor_signup_view(self):
        view = resolve("/signup/doctor/")
        self.assertEqual(view.func.__name__, PatientSignUpView.as_view().__name__)
