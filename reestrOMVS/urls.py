from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('omvs/IO', views.IO_OMVS, name='omvs_IO'),
    path('omvs/SI', views.SI_OMVS, name='omvs_SI'),
    path('omvs/VO', views.VO_OMVS, name='omvs_VO'),
    path('omvs/SM', views.SM_OMVS, name='omvs_SM'),
    path('omvs/OP', views.OP_OMVS, name='omvs_OP'),
    path('omvs/VOA', views.VOA_OMVS, name='omvs_VOA'),
    path('omvs/VU', views.VU_OMVS, name='omvs_VU'),
    path('omvs/SPI', views.SPI_OMVS, name='omvs_SPI'),
    path('detail/omvs_si/<int:pk>', views.equipment_SI_OMVSDatailView, name='omvs_SI_DATAIL'), 
    path('detail/omvs_io/<int:pk>', views.equipment_IO_OMVSDatailView, name='omvs_IO_DATAIL'), 
    path('detail/omvs_vo/<int:pk>', views.equipment_VO_OMVSDatailView, name='omvs_VO_DATAIL'), 
    path('detail/omvs_voa/<int:pk>', views.equipment_VOA_OMVSDatailView, name='omvs_VOA_DATAIL'),
    path('search/omvs/', views.search_OMVS, name='search_omvs'),
]