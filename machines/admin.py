from django.contrib import admin

# Models
from machines.models import Machine, Type, Rent


admin.site.register(Machine)
admin.site.register(Type)
admin.site.register(Rent)
