"""User views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):

	template_name = 'users/detail.html'
	slug_field = 'username'
	slug_url_kwarg = 'username'
	queryset = User.objects.all()
	context_object_name = 'user'

	def get_context_data(self, **kwargs):
		pass


class SignupView(FormView):

	template_name = 'users/signup.html'
	form_class = SignupForm
	success_url = reverse_lazy('users:login')

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):

	template_name = 'users/update_profile.html'
	model = Profile
	fields = ['phone_number', 'address', 'picture']

	def get_object(self):
		return self.request.user.profile

	def get_success_url(self):
		username = self.object.user.username
		return reverse('user:detail', kwargs={'username': username})


class LoginView(auth_views.LoginView):

	template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):

	template_name = 'users/logout.html'
