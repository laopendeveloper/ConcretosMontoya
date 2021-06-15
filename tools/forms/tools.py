"""Machine forms."""

# Django
from django import forms
from django.forms import (
	ModelForm,
	TextInput,
	EmailInput,
	Textarea,
	NumberInput,
	Select,
	FileInput,
    DateTimeInput
)
from datetimewidget.widgets import DateTimeWidget

# Models
from tools.models import Tool, ToolType


class ToolForm(ModelForm):
	"""Tool model form."""

	class Meta:
		"""Form settings."""
		
		model = Tool
		fields = (
			'name',
			'tool_type',
			'picture'
		)
		widgets = {
			'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nombre'
            }),
            'tool_type': Select(attrs={
                'class': "form-control",
                'placeholder': 'Tipo'
            }),
            'picture': FileInput(attrs={
                'class': "form-control",
                'placeholder': 'Tipo'
            })
		}