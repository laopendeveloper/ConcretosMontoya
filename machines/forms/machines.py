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
from machines.models import Machine, Rent


class MachineForm(ModelForm):
	"""Machine model form."""

	class Meta:
		"""Form settings."""
		
		model = Machine
		fields = (
			'name',
			'serial_number',
			'model',
			'description',
			'price',
			'machine_type',
			'photo'
		)
		widgets = {
			'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nombre'
            }),
            'serial_number': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Número de serie'
            }),
            'model': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Modelo'
            }),
            'description': Textarea(attrs={
                'class': "form-control",
                'rows': '5',
                'placeholder': 'Descripción'
            }),
            'price': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Precio'
            }),
            'machine_type': Select(attrs={
                'class': "form-control",
                'placeholder': 'Tipo'
            }),
            'photo': FileInput(attrs={
                'class': "form-control",
                'placeholder': 'Tipo'
            })
            # 'serial_number': EmailInput(attrs={
            #     'class': "form-control", 
            #     'style': 'max-width: 300px;',
            #     'placeholder': 'Email'
            # })
		}