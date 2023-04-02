from django.contrib import admin

from .models import Teacher, Bastaush


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'job')
    search_fields = ('name',)


class BastaushAdmin(admin.ModelAdmin):
    list_display = ('name', 'job')
    search_fields = ('name',)


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Bastaush, BastaushAdmin)