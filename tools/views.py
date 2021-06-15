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
from tools.forms import ToolForm

# Models
from tools.models import Tool, ToolType

# Python
from datetime import datetime


class ToolListView(LoginRequiredMixin, ListView):
	"""Return all tools."""

	template_name = 'list.html'
	model = Tool
	ordering = ('-created',)
	paginated_by = 30
	context_object_name = 'tools'


class ToolDetailView(LoginRequiredMixin, DetailView):

	template_name = 'tool_detail.html'
	queryset = Tool.objects.all()
	context_object_name = 'tool'

	def get_context_data(self, **kwargs):
		context = super(ToolDetailView, self).get_context_data(**kwargs)
		context['type'] = ToolType.objects.get(tool=kwargs['object'])
		return context


class CreateToolView(LoginRequiredMixin, CreateView):

	template_name = 'new_tool.html'
	form_class = ToolForm
	success_url = reverse_lazy('tools:list')


class UpdateToolView(LoginRequiredMixin, UpdateView):

	template_name = 'new_tool.html'
	model = Tool
	form_class = ToolForm

	def get_success_url(self):
		pk = self.kwargs['pk']
		return reverse_lazy('tools:detail', kwargs={'pk': pk})
