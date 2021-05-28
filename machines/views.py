# Django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

# Forms
from machines.forms import MachineForm

# Models
from machines.models import Machine


class MachineListView(LoginRequiredMixin, ListView):
	"""Return all machines."""

	template_name = 'feed.html'
	model = Machine
	ordering = ('-created',)
	paginated_by = 30
	context_object_name = 'machines'


class MachineDetailView(LoginRequiredMixin, DetailView):

	template_name = 'detail.html'
	queryset = Machine.objects.all()
	context_object_name = 'machine'


class CreateMachineView(LoginRequiredMixin, CreateView):

	template_name = 'new.html'
	form_class = MachineForm
	success_url = reverse_lazy('machines:feed')
