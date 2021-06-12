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

