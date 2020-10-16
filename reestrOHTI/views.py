from django.shortcuts import render, HttpResponse
from . models import Equipment_SI_OHTI, Equipment_IO_OHTI, Equipment_VO_OHTI, Equipment_SM_OHTI, Equipment_OP_OHTI, Equipment_VOA_OHTI, Equipment_VU_OHTI, Equipment_SPI_OHTI
from . models import Equip_SI_part_OHTI, Equip_IO_part_OHTI, Equip_VO_part_OHTI, Equip_VOA_part_OHTI
from django.views.generic import DetailView
from django.db.models import Q

# Create your views here.

def SI_OHTI(request):
    data={'base':Equipment_SI_OHTI.objects.all()}
    return render(request, 'reestrOHTI/SI.html',data)
    
    
def IO_OHTI(request):
    data={'base':Equipment_IO_OHTI.objects.all()}
    return render(request, 'reestrOHTI/IO.html', data)

def VO_OHTI(request):
    data={'base':Equipment_VO_OHTI.objects.all()}
    return render(request, 'reestrOHTI/VO.html', data)

def SM_OHTI(request):
    data={'base':Equipment_SM_OHTI.objects.all()}
    return render(request, 'reestrOHTI/SM.html', data)

def OP_OHTI(request):
    data={'base':Equipment_OP_OHTI.objects.all()}
    return render(request, 'reestrOHTI/OP.html', data)

def VOA_OHTI(request):
    data={'base':Equipment_VOA_OHTI.objects.all()}
    return render(request, 'reestrOHTI/VOA.html', data)

def VU_OHTI(request):
    data={'base':Equipment_VU_OHTI.objects.all()}
    return render(request, 'reestrOHTI/VU.html', data)
    
def SPI_OHTI(request):
    data={'base':Equipment_SPI_OHTI.objects.all()}
    return render(request, 'reestrOHTI/SPI.html', data)



def equipment_SI_OHTIDatailView(request, pk):
    equip_obj=Equipment_SI_OHTI.objects.get(pk=pk)
    parts_obj=Equip_SI_part_OHTI.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOHTI/equipment_datail.html', context= dict)

def equipment_IO_OHTIDatailView(request, pk):
    equip_obj=Equipment_IO_OHTI.objects.get(pk=pk)
    parts_obj=Equip_IO_part_OHTI.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOHTI/equipment_datail.html', context= dict)


def equipment_VO_OHTIDatailView(request, pk):
    equip_obj=Equipment_VO_OHTI.objects.get(pk=pk)
    parts_obj=Equip_VO_part_OHTI.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOHTI/equipment_datail.html', context= dict)

def equipment_VOA_OHTIDatailView(request, pk):
    equip_obj=Equipment_VOA_OHTI.objects.get(pk=pk)
    parts_obj=Equip_VOA_part_OHTI.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrOHTI/equipment_datail.html', context= dict)




def search_OHTI(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        search_SI_OHTI = Equipment_SI_OHTI.objects.filter(
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

        search_IO_OHTI = Equipment_IO_OHTI.objects.filter(
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

        search_VO_OHTI = Equipment_VO_OHTI.objects.filter(
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

        search_SM_OHTI = Equipment_SM_OHTI.objects.filter(
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

        search_OP_OHTI = Equipment_OP_OHTI.objects.filter(
        Q(name_of_equipment__icontains = q)|
        Q(model_type__icontains = q)|
        Q(company__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(invent_number__icontains = q)|
        Q(date_start_usage__icontains = q)|
        Q(location_lab__icontains = q)|
        Q(fact__icontains = q))

        search_VOA_OHTI = Equipment_VOA_OHTI.objects.filter(
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

        search_VU_OHTI = Equipment_VU_OHTI.objects.filter(
        Q(name_of_equipment__icontains = q)|
        Q(model_type__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(invent_number__icontains = q)|
        Q(date_manufactur__icontains = q)|
        Q(date_start_usage__icontains = q)|
        Q(location_lab__icontains = q)|
        Q(fact__icontains = q))

        search_SPI_OHTI = Equipment_SPI_OHTI.objects.filter(
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

        parts_SI_OHTI=Equip_SI_part_OHTI.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 

        parts_IO_OHTI=Equip_IO_part_OHTI.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 

        parts_VO_OHTI=Equip_VO_part_OHTI.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 

        parts_VOA_OHTI=Equip_VOA_part_OHTI.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 
        return render(request, 'reestrOHTI/search_result.html',{'search_SI_OHTI':search_SI_OHTI,'search_IO_OHTI':search_IO_OHTI,
        'search_VO_OHTI':search_VO_OHTI,'search_SM_OHTI':search_SM_OHTI,'search_OP_OHTI':search_OP_OHTI,'search_VOA_OHTI':search_VOA_OHTI,
        'search_VU_OHTI':search_VU_OHTI,'search_SPI_OHTI':search_SPI_OHTI,'parts_SI_OHTI':parts_SI_OHTI,
        'parts_IO_OHTI':parts_IO_OHTI,'parts_VO_OHTI':parts_VO_OHTI,'parts_VOA_OHTI':parts_VOA_OHTI,'query':q})      
    else:
        return HttpResponse('Введите что-нибудь в строке поиска')