from django.urls import path, include
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('omvoig_reestr_chromat', views.chromat_spectr, name='omvoig_chromat'),
    path('omvoig_reestr_analys_gruntov', views.analys_gruntov, name='omvoig_analys_gruntov'),
    path('omvoig_reestr_analys_vod', views.analys_vod, name='omvoig_analys_vod'),
    path('omvoig_reestr_toxic', views.toxic, name='omvoig_toxic'),
    path('omvoig_reestr_v_otdele', views.omvoig_v_otdete, name='omvoig_v_otdete'),

    path('omff_rad_control', views.rad_control, name='omff_rad_control'),
    path('omff_v_otdete', views.v_otdele, name='omff_v_otdele'),

    path('omvs_air_control', views.air_control, name='omvs_air_control'),
    path('omvs_factury_emission', views.factury_emission, name='omvs_factury_emission'),
    path('omvs_v_otdete', views.omvs_v_otdele, name='omvs_v_otdele'),
    
    path('ohti_v_otdete', views.ohti_v_otdele, name='ohti_v_otdele'),

    path('omoir_v_otdete', views.omoir_v_otdele, name='omoir_v_otdele'),

    path('po_v_otdete', views.po_v_otdele, name='po_v_otdele'),

    path('orimp_v_otdete', views.orimp_v_otdele, name='orimp_v_otdele'),

    path('ruk_v_otdete', views.ruk_v_otdele, name='ruk_v_otdele'),



    path('detail_omvoig/<int:pk>', views.personal_OMVOig_DatailView, name='omvoig_personal_datail'), 

    path('detail_ohti/<int:pk>', views.personal_OHTI_DatailView, name='ohti_personal_datail'), 

    path('detail_omvs/<int:pk>', views.personal_OMVS_DatailView, name='omvs_personal_datail'), 

    path('detail_omff/<int:pk>', views.personal_OMFF_DatailView, name='omff_personal_datail'),

    path('detail_omoir/<int:pk>', views.personal_OMOIR_DatailView, name='omoir_personal_datail'),

    path('detail_orimp/<int:pk>', views.personal_ORIMP_DatailView, name='orimp_personal_datail'),

    path('detail_po/<int:pk>', views.personal_PO_DatailView, name='opo_personal_datail'),

    path('detail_ruk/<int:pk>', views.personal_RUK_DatailView, name='ruk_personal_datail'),
]