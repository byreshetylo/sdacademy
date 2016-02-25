from django.contrib import admin
from models import Student


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = ['name', 'email', 'skype']
    list_filter = ['courses']


admin.site.register(Student, StudentAdmin)
