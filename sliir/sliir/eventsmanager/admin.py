from django.contrib import admin

from .models import Event
from .models import PrivateGoal

admin.site.register(Event)
admin.site.register(PrivateGoal)
