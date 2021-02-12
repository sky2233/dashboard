from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import *

# Register your models here.
@admin.register(Internship)
class ticket(admin.ModelAdmin):
    list_display = ("ticket_title", "ticket_created")