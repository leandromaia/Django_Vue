from django.contrib import admin
from .models import Person


class PersonDetailAdmin(admin.ModelAdmin):
    list_display = ("first_name", "email")



admin.site.register(Person,PersonDetailAdmin)