from django.contrib import admin
from models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'skype', 'description']
    #list_filter = [is_staff()]

    def is_staff(self):
        return Coach.is_staff()

admin.site.register(Coach, CoachAdmin)
