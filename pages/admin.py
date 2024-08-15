from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rolled', 'courses')


admin.site.register(Student, StudentAdmin)