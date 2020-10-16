from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('ohti/IO', views.IO_OHTI, name='ohti_IO'),
    path('ohti/SI', views.SI_OHTI, name='ohti_SI'),
    path('ohti/VO', views.VO_OHTI, name='ohti_VO'),
    path('ohti/SM', views.SM_OHTI, name='ohti_SM'),
    path('ohti/OP', views.OP_OHTI, name='ohti_OP'),
    path('ohti/VOA', views.VOA_OHTI, name='ohti_VOA'),
    path('ohti/VU', views.VU_OHTI, name='ohti_VU'),
    path('ohti/SPI', views.SPI_OHTI, name='ohti_SPI'),
    path('detail/ohti_si/<int:pk>', views.equipment_SI_OHTIDatailView, name='ohti_SI_DATAIL'), 
    path('detail/ohti_io/<int:pk>', views.equipment_IO_OHTIDatailView, name='ohti_IO_DATAIL'), 
    path('detail/ohti_vo/<int:pk>', views.equipment_VO_OHTIDatailView, name='ohti_VO_DATAIL'), 
    path('detail/ohti_voa/<int:pk>', views.equipment_VOA_OHTIDatailView, name='ohti_VOA_DATAIL'),
    path('search/ohti/', views.search_OHTI, name='search_ohti'),
]