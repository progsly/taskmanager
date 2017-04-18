from django.contrib import admin
from .models import Task, Done

admin.site.register(Task)
admin.site.register(Done)
