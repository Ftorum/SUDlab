from django.shortcuts import render, HttpResponse
from . models import Equipment_SI_OMVS, Equipment_IO_OMVS, Equipment_VO_OMVS, Equipment_SM_OMVS, Equipment_OP_OMVS, Equipment_VOA_OMVS, Equipment_VU_OMVS, Equipment_SPI_OMVS
from . models import Equip_SI_part_OMVS, Equip_IO_part_OMVS, Equip_VO_part_OMVS, Equip_VOA_part_OMVS
from django.views.generic import DetailView
from django.db.models import Q

# Create your views here.
def SI_OMVS(request):
    data={'base':Equipment_SI_OMVS.objects.all()}
    return render(request, 'reestrOMVS/SI.html',data)
    
    
def IO_OMVS(request):
    data={'base':Equipment_IO_OMVS.objects.all()}
    return render(request, 'reestrOMVS/IO.html', data)

def VO_OMVS(request):
    data={'base':Equipment_VO_OMVS.objects.all()}
    return render(request, 'reestrOMVS/VO.html', data)

def SM_OMVS(request):
    data={'base':Equipment_SM_OMVS.objects.all()}
    return render(request, 'reestrOMVS/SM.html', data)

def OP_OMVS(request):
    data={'base':Equipment_OP_OMVS.objects.all()}
    return render(request, 'reestrOMVS/OP.html', data)

def VOA_OMVS(request):
    data={'base':Equipment_VOA_OMVS.objects.all()}
    return render(request, 'reestrOMVS/VOA.html', data)

def VU_OMVS(request):
    data={'base':Equipment_VU_OMVS.objects.all()}
    return render(request, 'reestrOMVS/VU.html', data)
    
def SPI_OMVS(request):
    data={'base':Equipment_SPI_OMVS.objects.all()}
    return render(request, 'reestrOMVS/SPI.html', data)



def equipment_SI_OMVSDatailView(request, pk):
    equip_obj=Equipment_SI_OMVS.objects.get(pk=pk)
    parts_obj=Equip_SI_part_OMVS.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOMVS/equipment_datail.html', context= dict)

def equipment_IO_OMVSDatailView(request, pk):
    equip_obj=Equipment_IO_OMVS.objects.get(pk=pk)
    parts_obj=Equip_IO_part_OMVS.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOMVS/equipment_datail.html', context= dict)


def equipment_VO_OMVSDatailView(request, pk):
    equip_obj=Equipment_VO_OMVS.objects.get(pk=pk)
    parts_obj=Equip_VO_part_OMVS.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOMVS/equipment_datail.html', context= dict)

def equipment_VOA_OMVSDatailView(request, pk):
    equip_obj=Equipment_VOA_OMVS.objects.get(pk=pk)
    parts_obj=Equip_VOA_part_OMVS.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOMVS/equipment_datail.html', context= dict)


def search_OMVS(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        search_SI_OMVS = Equipment_SI_OMVS.objects.filter(
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

        search_IO_OMVS = Equipment_IO_OMVS.objects.filter(
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

        search_VO_OMVS = Equipment_VO_OMVS.objects.filter(
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

        search_SM_OMVS = Equipment_SM_OMVS.objects.filter(
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

        search_OP_OMVS = Equipment_OP_OMVS.objects.filter(
        Q(name_of_equipment__icontains = q)|
        Q(model_type__icontains = q)|
        Q(company__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(invent_number__icontains = q)|
        Q(date_start_usage__icontains = q)|
        Q(location_lab__icontains = q)|
        Q(fact__icontains = q))

        search_VOA_OMVS = Equipment_VOA_OMVS.objects.filter(
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

        search_VU_OMVS = Equipment_VU_OMVS.objects.filter(
        Q(name_of_equipment__icontains = q)|
        Q(model_type__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(invent_number__icontains = q)|
        Q(date_manufactur__icontains = q)|
        Q(date_start_usage__icontains = q)|
        Q(location_lab__icontains = q)|
        Q(fact__icontains = q))

        search_SPI_OMVS = Equipment_SPI_OMVS.objects.filter(
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

        parts_SI_OMVS=Equip_SI_part_OMVS.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 

        parts_IO_OMVS=Equip_IO_part_OMVS.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 

        parts_VO_OMVS=Equip_VO_part_OMVS.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 

        parts_VOA_OMVS=Equip_VOA_part_OMVS.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 
        return render(request, 'reestrOMVS/search_result.html',{'search_SI_OMVS':search_SI_OMVS,'search_IO_OMVS':search_IO_OMVS,
        'search_VO_OMVS':search_VO_OMVS,'search_SM_OMVS':search_SM_OMVS,'search_OP_OMVS':search_OP_OMVS,'search_VOA_OMVS':search_VOA_OMVS,
        'search_VU_OMVS':search_VU_OMVS,'search_SPI_OMVS':search_SPI_OMVS,'parts_SI_OMVS':parts_SI_OMVS,
        'parts_IO_OMVS':parts_IO_OMVS,'parts_VO_OMVS':parts_VO_OMVS,'parts_VOA_OMVS':parts_VOA_OMVS,'query':q})      
    else:
        return HttpResponse('Введите что-нибудь в строке поиска')