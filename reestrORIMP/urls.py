from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('orimp/IO', views.IO_ORIMP, name='orimp_IO'),
    path('orimp/SI', views.SI_ORIMP, name='orimp_SI'),
    path('orimp/VO', views.VO_ORIMP, name='orimp_VO'),
    path('orimp/ET', views.ET_ORIMP, name='orimp_ET'),
    path('orimp/RET', views.RET_ORIMP, name='orimp_RET'),
    path('detail/orimp_si/<int:pk>', views.equipment_SI_ORIMPDatailView, name='orimp_SI_DATAIL'), 
    path('detail/orimp_io/<int:pk>', views.equipment_IO_ORIMPDatailView, name='orimp_IO_DATAIL'), 
    path('detail/orimp_vo/<int:pk>', views.equipment_VO_ORIMPDatailView, name='orimp_VO_DATAIL'), 
    path('search/orimp/', views.search_ORIMP, name='search_orimp'),

]