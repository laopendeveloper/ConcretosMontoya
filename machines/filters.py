# Django filters
from django_filters

# Models
from machines.models import Machine


class MachineFilter(django_filters.FilterSet):
	class Meta:
		model = Machine
		fields = (
			'name',
			'serial_number',
			'model',
			'description',
			'price',
			'machine_type',
			'is_available',
			'rent_price'
		)
