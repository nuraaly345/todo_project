from django.contrib import admin
from .models import *

class ToDoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(ToDo)
