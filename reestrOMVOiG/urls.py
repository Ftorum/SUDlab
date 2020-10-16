from django.urls import path, include
from django.conf.urls.static import static
from . import views
from .views import equipment_SIDatailView

urlpatterns = [
    path('IO', views.IO, name='omvoig_IO'),
    path('SI', views.SI, name='omvoig_SI'),
    path('VO', views.VO, name='omvoig_VO'),
    path('SM', views.SM, name='omvoig_SM'),
    path('OP', views.OP, name='omvoig_OP'),
    path('VOA', views.VOA, name='omvoig_VOA'),
    path('VU', views.VU, name='omvoig_VU'),
    path('SPI', views.SPI, name='omvoig_SPI'),
    path('detail/si/<int:pk>', views.equipment_SIDatailView, name='omvoig_SI_DATAIL'), 
    path('detail/io/<int:pk>', views.equipment_IODatailView, name='omvoig_IO_DATAIL'), 
    path('detail/vo/<int:pk>', views.equipment_VODatailView, name='omvoig_VO_DATAIL'), 
    path('detail/voa/<int:pk>', views.equipment_VOADatailView, name='omvoig_VOA_DATAIL'), 
    path('search/omvoig/', views.search, name='search'),
]