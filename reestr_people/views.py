from django.shortcuts import render
from . models import OMVOiG_reestr, OMFF_reestr,OMVS_reestr,OHTI_reestr, OMOIR_reestr, PO_reestr,RUK_reestr,ORIMP_reestr
from reestrOMVOiG.models import Equipment_SI

# ОМВОиГ реестр персонала.
def chromat_spectr(request):
    data={'base': OMVOiG_reestr.objects.filter(group='Группа хроматографических и спектрометрических исследований')}
    return render(request, 'reestr_people/omvoig_chromat_spectr.html',data)

def analys_gruntov(request):
    data={'base': OMVOiG_reestr.objects.filter(group='Группа анализа грунтов')}
    return render(request, 'reestr_people/omvoig_chromat_spectr.html',data)

def analys_vod(request):
    data={'base': OMVOiG_reestr.objects.filter(group='Группа анализа природных и питьевых вод')}
    return render(request, 'reestr_people/omvoig_chromat_spectr.html',data)
def toxic(request):
    data={'base': OMVOiG_reestr.objects.filter(group='Группа токсикологических исследований')}
    return render(request, 'reestr_people/omvoig_chromat_spectr.html',data)
def omvoig_v_otdete(request):
    data={'base': OMVOiG_reestr.objects.filter(group='В отделе')}
    return render(request, 'reestr_people/omvoig_chromat_spectr.html',data)

# ОМФФ реестр персонала.
def rad_control(request):
    data={'base': OMFF_reestr.objects.filter(group='Группа радиационного контроля')}
    return render(request, 'reestr_people/omff.html',data)
def v_otdele(request):
    data={'base': OMFF_reestr.objects.filter(group='В отделе')}
    return render(request, 'reestr_people/omff.html',data)


# ОМВС реестр персонала.
def air_control(request):
    data={'base': OMVS_reestr.objects.filter(group='Группа контроля воздуха рабочей зоны')}
    return render(request, 'reestr_people/omvs.html',data)
def factury_emission(request):
    data={'base': OMVS_reestr.objects.filter(group='Группа по контролю промышленных выбросов и атмосферного воздуха')}
    return render(request, 'reestr_people/omvs.html',data)
def omvs_v_otdele(request):
    data={'base': OMVS_reestr.objects.filter(group='В отделе')}
    return render(request, 'reestr_people/omvs.html',data)

# ОХТИ реестр персонала.
def ohti_v_otdele(request):
    data={'base': OHTI_reestr.objects.all()}
    return render(request, 'reestr_people/ohti.html',data)

# ОМОиР реестр персонала.
def omoir_v_otdele(request):
    data={'base': OMOIR_reestr.objects.all()}
    return render(request, 'reestr_people/omoir.html',data)

# ПО реестр персонала.
def po_v_otdele(request):
    data={'base': PO_reestr.objects.all()}
    return render(request, 'reestr_people/po.html',data)

# ОРиМР реестр персонала.
def orimp_v_otdele(request):
    data={'base': ORIMP_reestr.objects.all()}
    return render(request, 'reestr_people/orimp.html',data)

# Руководство реестр персонала.
def ruk_v_otdele(request):
    data={'base': RUK_reestr.objects.all()}
    return render(request, 'reestr_people/ruk.html',data)







def personal_OMVOig_DatailView(request, pk):
    persona=OMVOiG_reestr.objects.get(pk=pk)

    dict={'object':persona}
    return render(request,'reestr_people/reest_datails.html', context= dict)

def personal_OHTI_DatailView(request, pk):
    persona=OHTI_reestr.objects.get(pk=pk)

    dict={'object':persona}
    return render(request,'reestr_people/reest_datails.html', context= dict)

def personal_OMVS_DatailView(request, pk):
    persona=OMVS_reestr.objects.get(pk=pk)

    dict={'object':persona}
    return render(request,'reestr_people/reest_datails.html', context= dict)

def personal_OMFF_DatailView(request, pk):
    persona=OMFF_reestr.objects.get(pk=pk)

    dict={'object':persona}
    return render(request,'reestr_people/reest_datails.html', context= dict)

def personal_OMOIR_DatailView(request, pk):
    persona=OMOIR_reestr.objects.get(pk=pk)

    dict={'object':persona}
    return render(request,'reestr_people/reest_datails.html', context= dict)

def personal_ORIMP_DatailView(request, pk):
    persona=ORIMP_reestr.objects.get(pk=pk)

    dict={'object':persona}
    return render(request,'reestr_people/reest_datails.html', context= dict)

def personal_PO_DatailView(request, pk):
    persona=PO_reestr.objects.get(pk=pk)

    dict={'object':persona}
    return render(request,'reestr_people/reest_datails.html', context= dict)

def personal_RUK_DatailView(request, pk):
    persona=RUK_reestr.objects.get(pk=pk)

    dict={'object':persona}
    return render(request,'reestr_people/reest_datails.html', context= dict)