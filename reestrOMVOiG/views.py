from django.shortcuts import render, HttpResponse
from . models import Equipment_SI, Equipment_IO, Equipment_VO, Equipment_SM, Equipment_OP, Equipment_VOA, Equipment_VU,Equipment_SPI
from . models import Equip_SI_part, Equip_IO_part, Equip_VO_part, Equip_VOA_part
from django.views.generic import DetailView
from django.db.models import Q

# Create your views here.

def SI(request):
    data={'base':Equipment_SI.objects.all()}
    return render(request, 'reestrOMVOiG/SI.html',data)
    
    
def IO(request):
    data={'base':Equipment_IO.objects.all()}
    return render(request, 'reestrOMVOiG/IO.html', data)

def VO(request):
    data={'base':Equipment_VO.objects.all()}
    return render(request, 'reestrOMVOiG/VO.html', data)

def SM(request):
    data={'base':Equipment_SM.objects.all()}
    return render(request, 'reestrOMVOiG/SM.html', data)

def OP(request):
    data={'base':Equipment_OP.objects.all()}
    return render(request, 'reestrOMVOiG/OP.html', data)

def VOA(request):
    data={'base':Equipment_VOA.objects.all()}
    return render(request, 'reestrOMVOiG/VOA.html', data)

def VU(request):
    data={'base':Equipment_VU.objects.all()}
    return render(request, 'reestrOMVOiG/VU.html', data)
    
def SPI(request):
    data={'base':Equipment_SPI.objects.all()}
    return render(request, 'reestrOMVOiG/SPI.html', data)

def equipment_SIDatailView(request, pk):
    equip_obj=Equipment_SI.objects.get(pk=pk)
    parts_obj=Equip_SI_part.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOMVOiG/equipment_datail.html', context= dict)


def equipment_IODatailView(request, pk):
    equip_obj=Equipment_IO.objects.get(pk=pk)
    parts_obj=Equip_IO_part.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOMVOiG/equipment_datail.html', context= dict)


def equipment_VODatailView(request, pk):
    equip_obj=Equipment_VO.objects.get(pk=pk)
    parts_obj=Equip_VO_part.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOMVOiG/equipment_datail.html', context= dict)

def equipment_VOADatailView(request, pk):
    equip_obj=Equipment_VOA.objects.get(pk=pk)
    parts_obj=Equip_VOA_part.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOMVOiG/equipment_datail.html', context= dict)



def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        search_SI = Equipment_SI.objects.filter(
        Q(name_of_equipment__icontains = q)|
        Q(model_type__icontains = q)|
        Q(number_gosreestr__icontains = q)|
        Q(company__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(invent_number__icontains = q)|
        Q(date_manufactur__icontains = q)|
        Q(date_start_usage__icontains = q)|
        Q(location_lab__icontains = q)|
        Q(microclimate__icontains = q)|
        Q(organization_check__icontains = q)|
        Q(range_check__icontains = q)|
        Q(last_verification__icontains = q)|
        Q(last_maintaince__icontains = q)|
        Q(fact__icontains = q))

        search_IO = Equipment_IO.objects.filter(
        Q(name_of_equipment__icontains = q)|
        Q(model_type__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(invent_number__icontains = q)|
        Q(date_manufactur__icontains = q)|
        Q(date_start_usage__icontains = q)|
        Q(location_lab__icontains = q)|
        Q(microclimate__icontains = q)|
        Q(organization_check__icontains = q)|
        Q(range_check__icontains = q)|
        Q(last_verification__icontains = q)|
        Q(last_maintaince__icontains = q)|
        Q(fact__icontains = q))

        search_VO = Equipment_VO.objects.filter(
        Q(name_of_equipment__icontains = q)|
        Q(model_type__icontains = q)|
        Q(company__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(invent_number__icontains = q)|
        Q(date_manufactur__icontains = q)|
        Q(date_start_usage__icontains = q)|
        Q(location_lab__icontains = q)|
        Q(microclimate__icontains = q)|
        Q(fact__icontains = q))

        search_SM = Equipment_SM.objects.filter(
        Q(name_of_equipment__icontains = q)|
        Q(model_type__icontains = q)|
        Q(company__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(invent_number__icontains = q)|
        Q(date_manufactur__icontains = q)|
        Q(date_start_usage__icontains = q)|
        Q(location_lab__icontains = q)|
        Q(microclimate__icontains = q)|
        Q(fact__icontains = q))

        search_OP = Equipment_OP.objects.filter(
        Q(name_of_equipment__icontains = q)|
        Q(model_type__icontains = q)|
        Q(company__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(invent_number__icontains = q)|
        Q(date_start_usage__icontains = q)|
        Q(location_lab__icontains = q)|
        Q(fact__icontains = q))

        search_VOA = Equipment_VOA.objects.filter(
        Q(name_of_equipment__icontains = q)|
        Q(model_type__icontains = q)|
        Q(company__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(invent_number__icontains = q)|
        Q(date_manufactur__icontains = q)|
        Q(date_start_usage__icontains = q)|
        Q(location_lab__icontains = q)|
        Q(microclimate__icontains = q)|
        Q(organization_check__icontains = q)|
        Q(range_check__icontains = q)|
        Q(last_verification__icontains = q)|
        Q(last_maintaince__icontains = q)|
        Q(fact__icontains = q))

        search_VU = Equipment_VU.objects.filter(
        Q(name_of_equipment__icontains = q)|
        Q(model_type__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(invent_number__icontains = q)|
        Q(date_manufactur__icontains = q)|
        Q(date_start_usage__icontains = q)|
        Q(location_lab__icontains = q)|
        Q(fact__icontains = q))

        search_SPI = Equipment_SPI.objects.filter(
        Q(name_of_equipment__icontains = q)|
        Q(model_type__icontains = q)|
        Q(company__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(invent_number__icontains = q)|
        Q(date_manufactur__icontains = q)|
        Q(date_start_usage__icontains = q)|
        Q(location_lab__icontains = q)|
        Q(date_end_usage__icontains = q)|
        Q(fact__icontains = q))
        #запчасти и расходные материалы

        parts_SI=Equip_SI_part.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 

        parts_IO=Equip_IO_part.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 

        parts_VO=Equip_VO_part.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 

        parts_VOA=Equip_VO_part.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 
        return render(request, 'reestrOMVOiG/search_result.html',{'search_SI':search_SI,'search_IO':search_IO,'search_VO':search_VO,
        'search_SM':search_SM,'search_OP':search_OP,'search_VOA':search_VOA,'search_VU':search_VU,'search_SPI':search_SPI,'parts_SI':parts_SI,
        'parts_IO':parts_IO,'parts_VO':parts_VO,'parts_VOA':parts_VOA,'query':q})      
    else:
        return HttpResponse('Введите что-нибудь в строке поиска')
