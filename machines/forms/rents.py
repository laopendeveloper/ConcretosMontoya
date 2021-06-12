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


class RentForm(ModelForm):

    def __init__(self, machine_pk, *args, **kwargs):
        super(RentForm, self).__init__(*args, **kwargs)
        print(machine_pk)
        self.fields['machine'].widget = forms.TextInput(attrs={
            'class': "form-control hidden-input",
            'placeholder': 'Cliente',
            'value': machine_pk
        })

    class Meta:

        model = Rent
        fields = (
            'client',
            'machine',
            'rent_from',
            'rent_to',
            'notes'
        )
        widgets = {
            # 'client': Select(attrs={
            #     'class': "form-control",
            #     'placeholder': 'Cliente'
            # }),
            'client': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Cliente'
            }),
            'machine': TextInput(),
            'rent_from': DateTimeInput(attrs={
                'id': 'datetimepicker1',
                'class': "form-control datetimepicker-input",
                'placeholder': 'Escoje la fecha de inicio',
                'data-target': '#datetimepicker1'
            }),
            'rent_to': DateTimeInput(attrs={
                'id': 'datetimepicker2',
                'class': "form-control datetimepicker-input",
                'placeholder': 'Escoje la fecha de termino',
                'data-target': '#datetimepicker2'
            }),
            'notes': Textarea(attrs={
                'class': "form-control",
                'rows': '5',
                'placeholder': 'Notas'
            }),
        }

    # def save(self, commit=True):
    #     print(self.cleaned_data['machine'])
    #     machine = Machine.objects.get(pk=self.cleaned_data['machine'])
    #     self.cleaned_data['machine'] = machine
    #     return super(RentForm, self).save(commit)

    # def clean_machine(self):
    #     machineid = self.cleaned_data['machine']
    #     print(self.cleaned_data)
    #     print(machineid.pk)
    #     try:
    #         machine = Machine.objects.get(pk=machineid.pk)
    #     except Machine.DoesNotExists:
    #         raise ValidationError('There is not machine with pk {}'.format(machine))
    #     return machine.pk
