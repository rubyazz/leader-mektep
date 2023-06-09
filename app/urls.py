from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
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
    path('menu/', views.menu, name='menu'),
    path('eng/ata-ana-kom/', views.my_view_eng, name='my_view_eng'), # english
    path('eng/akimshilik/', views.akimshilik_eng, name='akimshilik_eng'),#server error
    path('eng/activities/', views.activities_eng, name='activities_eng'),
    path('eng/akeler/', views.akeler_eng, name='akeler_eng'),
    path('eng/bailanys/', views.bailanys_eng, name='bailanys_eng'),
    path('eng/index/', views.index_eng, name='index_eng'),
    path('eng/ata-ana/', views.ata_ana_eng, name='ata_ana_eng'),
    path('eng/gallery/', views.gallery_eng, name='gallery_eng'),
    path('eng/forma/', views.forma_eng, name='forma_eng'),
    path('eng/kundylyktar/', views.kundylyktar_eng, name='kundylyktar_eng'),
    path('eng/kirispe/', views.kirispe_eng, name='kirispe_eng'),
    path('eng/kuntizbe/', views.kuntizbe_eng, name='kuntizbe_eng'),
    path('eng/kuzhat/', views.kuzhat_eng, name='kuzhat_eng'),
    path('eng/oob-zhumys/', views.oob_zhumys_eng, name='oob_zhumys_eng'),
    path('eng/pupils/', views.pupils_eng, name='pupils_eng'),
    path('eng/suraktar/', views.suraktar_eng, name='suraktar_eng'),
    path('eng/tarbie_zhumystary2/', views.tarbie_zhumystary2_eng, name='tarbie_zhumystary2_eng'),
    path('eng/tarbie_zhumysy/', views.tarbie_zhumysy_eng, name='tarbie_zhumysy_eng'),
    path('eng/teachers/', views.teacher_list_eng, name='teachers_eng'),
    path('eng/uirme/', views.uirme_eng, name='uirme_eng'),
    path('bastaush/', views.bastaush, name='bastaush'), # second teachers
    path('eng/bastaush/', views.bastaush_eng, name='bastaush_eng'),
    path('eng/uirme_zhetekshileri/', views.uirme_zhetekshileri_eng, name='uirme_zhetekshileri_eng'),
    path('uirme_zhetekshileri/', views.uirme_zhetekshileri, name='uirme_zhetekshileri'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
