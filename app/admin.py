from django.contrib import admin

from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'job')
    search_fields = ('name',)


admin.site.register(Teacher, TeacherAdmin)
