# Django
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic import (
	CreateView,
	UpdateView,
	DetailView,
	ListView
)

# Forms
from machines.forms import MachineForm, RentForm

# Models
from machines.models import Machine, Rent

# Python
from datetime import datetime


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

	def get_context_data(self, **kwargs):
		print(kwargs['object'])
		context = super(MachineDetailView, self).get_context_data(**kwargs)
		context['rent'] = Rent.objects.filter(machine=kwargs['object'])
		return context


class CreateMachineView(LoginRequiredMixin, CreateView):

	template_name = 'new.html'
	form_class = MachineForm
	success_url = reverse_lazy('machines:feed')


class UpdateMachineView(LoginRequiredMixin, UpdateView):

	template_name = 'new.html'
	model = Machine
	form_class = MachineForm

	def get_success_url(self):
		pk = self.kwargs['pk']
		return reverse_lazy('machines:detail', kwargs={'pk': pk})


class RentMachineView(LoginRequiredMixin, FormView):

	template_name = 'rent.html'
	model = Rent

	def post(self, request, *args, **kwargs):
		
		client = request.POST['client']
		machine = Machine.objects.get(pk=int(request.POST['machine']))
		rent_from = request.POST['rent_from']
		rent_to = request.POST['rent_to']
		notes = request.POST['notes']

		# Format datetime
		rent_from = datetime.strptime(rent_from, '%Y/%m/%d %H:%M')
		rent_to = datetime.strptime(rent_to, '%Y/%m/%d %H:%M')

		try:
			Rent.objects.create(
				client=client,
				machine=machine,
				rent_from=rent_from,
				rent_to=rent_to,
				notes=notes
			)
		except Exception as e:
			print(e)

		machine.is_available = False
		machine.save()

		return redirect('machines:detail', pk=machine.pk)

	def get(self, request, pk):
		form_class = RentForm(machine_pk=pk)
		return render(request, self.template_name, {'form': form_class})


	def form_valid(self, form):
		print(form.cleaned_data)
		# print(form.instance.machine)
		# form.instance.machine = self.machine
		return super(RentMachineView, self).form_valid(form)

	def get_success_url(self):
		pk = self.kwargs['pk']
		return reverse_lazy('machines:detail', kwargs={'pk': pk})
