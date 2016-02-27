from django.contrib import admin
from models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'skype', 'description']
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')


admin.site.register(Coach, CoachAdmin)
