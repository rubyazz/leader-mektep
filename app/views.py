from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Teacher, Bastaush


def teacher_list(request):
    qs = Teacher.objects.all()
    lst = Paginator(qs, 3)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, }
    return render(request, 'teachers.html', context)


def bastaush(request):
    qs = Bastaush.objects.all()
    lst = Paginator(qs, 3)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, }
    return render(request, 'bastaush.html', context)



def teacher_list_eng(request):
    qs = Teacher.objects.all()
    lst = Paginator(qs, 3)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, }
    return render(request, 'eng/teachers-en.html', context)

def bastaush_eng(request):
    qs = Bastaush.objects.all()
    lst = Paginator(qs, 3)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, }
    return render(request, 'eng/bastaush_en.html', context)
# return func of templates

def index(request):
    return render(request, 'index.html')

def uirme_zhetekshileri(request):
    return render(request, 'uirme_zhetekshileri.html')

def uirme_zhetekshileri_eng(request):
    return render(request, 'eng/uirme_zhetekshileri-en.html')

def menu(request):
    return render(request, 'menu.html')


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

# English
def my_view_eng(request):
    return render(request, 'eng/ata-ana-kom-en.html')

def akimshilik_eng(request):
    return render(request, 'eng/akimshilik-en.html')

def activities_eng(request):
    return render(request, 'eng/activities-en.html')

def akeler_eng(request):
    return render(request, 'eng/akeler-en.html')

def bailanys_eng(request):
    return render(request, 'eng/bailanys-en.html')

def index_eng(request):
    return render(request, 'eng/index-en.html')

def ata_ana_eng(request):
    return render(request, 'eng/ata-ana-en.html')

def gallery_eng(request):
    return render(request, 'eng/gallery-en.html')

def forma_eng(request):
    return render(request, 'eng/forma-en.html')

def kundylyktar_eng(request):
    return render(request, 'eng/kundylyktar-en.html')

def kirispe_eng(request):
    return render(request, 'eng/kirispe-en.html')

def kuntizbe_eng(request):
    return render(request, 'eng/kuntizbe-en.html')

def kuzhat_eng(request):
    return render(request, 'eng/kuzhat-en.html')

def oob_zhumys_eng(request):
    return render(request, 'eng/oob-zhumys-en.html')

def pupils_eng(request):
    return render(request, 'eng/pupils-en.html')

def suraktar_eng(request):
    return render(request, 'eng/suraktar-en.html')

def tarbie_zhumystary2_eng(request):
    return render(request, 'eng/tarbie_zhumystary2-en.html')

def tarbie_zhumysy_eng(request):
    return render(request, 'eng/tarbie_zhumysy-en.html')

def teachers_eng(request):
    return render(request, 'eng/teachers-en.html')

def uirme_eng(request):
    return render(request, 'eng/uirme-en.html')

