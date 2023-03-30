from django.shortcuts import render
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})
