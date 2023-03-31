from django.shortcuts import render
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'tea.html', {'teachers': teachers})

# return func of templates

def index(request):
    return render(request, 'index.html')


def activities(request):
    return render(request, 'activities.html')


def pupils(request):
    return render(request, 'pupils.html')


def kundylyktar(request):
    return render(request, 'kundylyktar.html')


def kirispe(request):
    return render(request, 'kirispe.html')


def tarbie_zhumysy(request):
    return render(request, 'tarbie_zhumysy.html')


def kuzhat(request):
    return render(request, 'kuzhat.html')


def tarbie_zhumystary2(request):
    return render(request, 'tarbie_zhumystary2.html')


def akimshilik(request):
    return render(request, 'akimshilik.html')


def suraktar(request):
    return render(request, 'suraktar.html')


def akeler(request):
    return render(request, 'akeler.html')


def oob_zhumys(request):
    return render(request, 'oob-zhumys.html')


def ata_ana(request):
    return render(request, 'ata-ana.html')


def kuntizbe(request):
    return render(request, 'kuntizbe.html')


def ata_ana_kom(request):
    return render(request, 'ata-ana-kom.html')


def gallery(request):
    return render(request, 'gallery.html')


def bailanys(request):
    return render(request, 'bailanys.html')


def forma(request):
    return render(request, 'forma.html')


def teachers(request):
    return render(request, 'teachers.html')


def uirme(request):
    return render(request, 'uirme.html')

