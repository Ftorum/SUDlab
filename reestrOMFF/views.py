from django.shortcuts import render, HttpResponse
from . models import Equipment_SI_OMFF, Equipment_IO_OMFF, Equipment_VO_OMFF, Equipment_SM_OMFF, Equipment_OP_OMFF, Equipment_VOA_OMFF, Equipment_VU_OMFF, Equipment_SPI_OMFF
from . models import Equip_SI_part_OMFF, Equip_IO_part_OMFF, Equip_VO_part_OMFF, Equip_VOA_part_OMFF
from django.views.generic import DetailView
from django.db.models import Q

# Create your views here.
# Create your views here.
def SI_OMFF(request):
    data={'base':Equipment_SI_OMFF.objects.all()}
    return render(request, 'reestrOMFF/SI.html',data)
    
    
def IO_OMFF(request):
    data={'base':Equipment_IO_OMFF.objects.all()}
    return render(request, 'reestrOMFF/IO.html', data)

def VO_OMFF(request):
    data={'base':Equipment_VO_OMFF.objects.all()}
    return render(request, 'reestrOMFF/VO.html', data)

def SM_OMFF(request):
    data={'base':Equipment_SM_OMFF.objects.all()}
    return render(request, 'reestrOMFF/SM.html', data)

def OP_OMFF(request):
    data={'base':Equipment_OP_OMFF.objects.all()}
    return render(request, 'reestrOMFF/OP.html', data)

def VOA_OMFF(request):
    data={'base':Equipment_VOA_OMFF.objects.all()}
    return render(request, 'reestrOMFF/VOA.html', data)

def VU_OMFF(request):
    data={'base':Equipment_VU_OMFF.objects.all()}
    return render(request, 'reestrOMFF/VU.html', data)
    
def SPI_OMFF(request):
    data={'base':Equipment_SPI_OMFF.objects.all()}
    return render(request, 'reestrOMFF/SPI.html', data)



def equipment_SI_OMFFDatailView(request, pk):
    equip_obj=Equipment_SI_OMFF.objects.get(pk=pk)
    parts_obj=Equip_SI_part_OMFF.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOMFF/equipment_datail.html', context= dict)

def equipment_IO_OMFFDatailView(request, pk):
    equip_obj=Equipment_IO_OMFF.objects.get(pk=pk)
    parts_obj=Equip_IO_part_OMFF.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOMFF/equipment_datail.html', context= dict)


def equipment_VO_OMFFDatailView(request, pk):
    equip_obj=Equipment_VO_OMFF.objects.get(pk=pk)
    parts_obj=Equip_VO_part_OMFF.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOMFF/equipment_datail.html', context= dict)

def equipment_VOA_OMFFDatailView(request, pk):
    equip_obj=Equipment_VOA_OMFF.objects.get(pk=pk)
    parts_obj=Equip_VOA_part_OMFF.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOMFF/equipment_datail.html', context= dict)




def search_OMFF(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        search_SI_OMFF = Equipment_SI_OMFF.objects.filter(
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

        search_IO_OMFF = Equipment_IO_OMFF.objects.filter(
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

        search_VO_OMFF = Equipment_VO_OMFF.objects.filter(
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

        search_SM_OMFF = Equipment_SM_OMFF.objects.filter(
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

        search_OP_OMFF = Equipment_OP_OMFF.objects.filter(
        Q(name_of_equipment__icontains = q)|
        Q(model_type__icontains = q)|
        Q(company__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(invent_number__icontains = q)|
        Q(date_start_usage__icontains = q)|
        Q(location_lab__icontains = q)|
        Q(fact__icontains = q))

        search_VOA_OMFF = Equipment_VOA_OMFF.objects.filter(
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

        search_VU_OMFF = Equipment_VU_OMFF.objects.filter(
        Q(name_of_equipment__icontains = q)|
        Q(model_type__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(invent_number__icontains = q)|
        Q(date_manufactur__icontains = q)|
        Q(date_start_usage__icontains = q)|
        Q(location_lab__icontains = q)|
        Q(fact__icontains = q))

        search_SPI_OMFF = Equipment_SPI_OMFF.objects.filter(
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

        parts_SI_OMFF=Equip_SI_part_OMFF.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 

        parts_IO_OMFF=Equip_IO_part_OMFF.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 

        parts_VO_OMFF=Equip_VO_part_OMFF.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 

        parts_VOA_OMFF=Equip_VOA_part_OMFF.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 
        return render(request, 'reestrOMFF/search_result.html',{'search_SI_OHTI':search_SI_OMFF,'search_IO_OHTI':search_IO_OMFF,
        'search_VO_OMFF':search_VO_OMFF,'search_SM_OMFF':search_SM_OMFF,'search_OP_OMFF':search_OP_OMFF,'search_VOA_OMFF':search_VOA_OMFF,
        'search_VU_OMFF':search_VU_OMFF,'search_SPI_OMFF':search_SPI_OMFF,'parts_SI_OMFF':parts_SI_OMFF,
        'parts_IO_OMFF':parts_IO_OMFF,'parts_VO_OMFF':parts_VO_OMFF,'parts_VOA_OMFF':parts_VOA_OMFF,'query':q})      
    else:
        return HttpResponse('Введите что-нибудь в строке поиска')