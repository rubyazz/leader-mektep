from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tea/', views.teacher_list, name='teacher_list'),
    path('activities/', views.activities, name='activities'),
    path('pupils/', views.pupils, name='pupils'),
    path('kundylyktar/', views.kundylyktar, name='kundylyktar'),
    path('kirispe/', views.kirispe, name='kirispe'),
    path('tarbie_zhumysy/', views.tarbie_zhumysy, name='tarbie_zhumysy'),
    path('kuzhat/', views.kuzhat, name='kuzhat'),
    path('tarbie_zhumystary2/', views.tarbie_zhumystary2, name='tarbie_zhumystary2'),
    path('akimshilik/', views.akimshilik, name='akimshilik'),
    path('suraktar/', views.suraktar, name='suraktar'),
    path('akeler/', views.akeler, name='akeler'),
    path('oob-zhumys/', views.oob_zhumys, name='oob_zhumys'),
    path('ata-ana/', views.ata_ana, name='ata_ana'),
    path('kuntizbe/', views.kuntizbe, name='kuntizbe'),
    path('ata-ana-kom/', views.ata_ana_kom, name='ata_ana_kom'),
    path('gallery/', views.gallery, name='gallery'),
    path('bailanys/', views.bailanys, name='bailanys'),
    path('forma/', views.forma, name='forma'),
    path('teachers/', views.teacher_list, name='teachers'),
    path('uirme/', views.uirme, name='uirme'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
