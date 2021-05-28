from django.contrib import admin

# Models
from machines.models import Machine, Type


admin.site.register(Machine)
admin.site.register(Type)
