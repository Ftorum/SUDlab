from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('omff/IO', views.IO_OMFF, name='omff_IO'),
    path('omff/SI', views.SI_OMFF, name='omff_SI'),
    path('omff/VO', views.VO_OMFF, name='omff_VO'),
    path('omff/SM', views.SM_OMFF, name='omff_SM'),
    path('omff/OP', views.OP_OMFF, name='omff_OP'),
    path('omff/VOA', views.VOA_OMFF, name='omff_VOA'),
    path('omff/VU', views.VU_OMFF, name='omff_VU'),
    path('omff/SPI', views.SPI_OMFF, name='omff_SPI'),
    path('detail/omff_si/<int:pk>', views.equipment_SI_OMFFDatailView, name='omff_SI_DATAIL'), 
    path('detail/omff_io/<int:pk>', views.equipment_IO_OMFFDatailView, name='omff_IO_DATAIL'), 
    path('detail/omff_vo/<int:pk>', views.equipment_VO_OMFFDatailView, name='omff_VO_DATAIL'), 
    path('detail/omff_voa/<int:pk>', views.equipment_VOA_OMFFDatailView, name='omff_VOA_DATAIL'),
    path('search/omff/', views.search_OMFF, name='search_omff'),
]