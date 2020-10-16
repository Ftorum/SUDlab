from django.shortcuts import render, HttpResponse
from . models import Equipment_SI_ORIMP, Equipment_IO_ORIMP, Equipment_VO_ORIMP, Equipment_ET_ORIMP,Equipment_RET_ORIMP
from . models import Equip_SI_part_ORIMP, Equip_IO_part_ORIMP, Equip_VO_part_ORIMP
from django.views.generic import DetailView
from django.db.models import Q

# Create your views here.
# Create your views here.
def SI_ORIMP(request):
    data={'base':Equipment_SI_ORIMP.objects.all()}
    return render(request, 'reestrORIMP/SI.html',data)
    
    
def IO_ORIMP(request):
    data={'base':Equipment_IO_ORIMP.objects.all()}
    return render(request, 'reestrORIMP/IO.html', data)

def VO_ORIMP(request):
    data={'base':Equipment_VO_ORIMP.objects.all()}
    return render(request, 'reestrORIMP/VO.html', data)


def ET_ORIMP(request):
    data={'base':Equipment_ET_ORIMP.objects.all()}
    return render(request, 'reestrORIMP/ET.html', data)

def RET_ORIMP(request):
    data={'base':Equipment_RET_ORIMP.objects.all()}
    return render(request, 'reestrORIMP/RET.html', data)



def equipment_SI_ORIMPDatailView(request, pk):
    equip_obj=Equipment_SI_ORIMP.objects.get(pk=pk)
    parts_obj=Equip_SI_part_ORIMP.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrORIMP/equipment_datail.html', context= dict)

def equipment_IO_ORIMPDatailView(request, pk):
    equip_obj=Equipment_IO_ORIMP.objects.get(pk=pk)
    parts_obj=Equip_IO_part_ORIMP.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrORIMP/equipment_datail.html', context= dict)


def equipment_VO_ORIMPDatailView(request, pk):
    equip_obj=Equipment_VO_ORIMP.objects.get(pk=pk)
    parts_obj=Equip_VO_part_ORIMP.objects.filter(name_of_equip=equip_obj)

    dict={'partis':parts_obj,'equip':equip_obj}
    return render(request,'reestrORIMP/equipment_datail.html', context= dict)


def search_ORIMP(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        search_SI_ORIMP = Equipment_SI_ORIMP.objects.filter(
        Q(name_of_equipment_passport__icontains = q)|
        Q(equip_R3__icontains = q)|
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

        search_IO_ORIMP = Equipment_IO_ORIMP.objects.filter(
        Q(name_of_equipment_passport__icontains = q)|
        Q(equip_R3__icontains = q)|
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

        search_VO_ORIMP = Equipment_VO_ORIMP.objects.filter(
        Q(name_of_equipment_passport__icontains = q)|
        Q(equip_R3__icontains = q)|
        Q(model_type__icontains = q)|
        Q(company__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(invent_number__icontains = q)|
        Q(date_manufactur__icontains = q)|
        Q(date_start_usage__icontains = q)|
        Q(location_lab__icontains = q)|
        Q(microclimate__icontains = q)|
        Q(fact__icontains = q))

        search_ET_ORIMP = Equipment_ET_ORIMP.objects.filter(
        Q(reg_number__icontains = q)|
        Q(name_of_equipment_passport__icontains = q)|
        Q(name_of_equipment_measure__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(fact__icontains = q))

        search_RET_ORIMP = Equipment_RET_ORIMP.objects.filter(
        Q(reg_number__icontains = q)|
        Q(name_of_equipment_passport__icontains = q)|
        Q(name_of_equipment_measure__icontains = q)|
        Q(factury_number__icontains = q)|
        Q(scheme_of_verivication__icontains = q)|
        Q(fact__icontains = q))
        
        #запчасти и расходные материалы

        parts_SI_ORIMP=Equip_SI_part_ORIMP.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 

        parts_IO_ORIMP=Equip_IO_part_ORIMP.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 

        parts_VO_ORIMP=Equip_VO_part_ORIMP.objects.filter(
        Q(name_of_part__icontains = q)|
        Q(fact_number__icontains = q)) 


        return render(request, 'reestrORIMP/search_result.html',{'search_SI_ORIMP':search_SI_ORIMP,'search_IO_ORIMP':search_IO_ORIMP,
        'search_VO_ORIMP':search_VO_ORIMP,'search_ET_ORIMP':search_ET_ORIMP,'search_RET_ORIMP':search_RET_ORIMP,
        'parts_SI_ORIMP':parts_SI_ORIMP,'parts_IO_ORIMP':parts_IO_ORIMP,'parts_VO_ORIMP':parts_VO_ORIMP,'query':q})      
    else:
        return HttpResponse('Введите что-нибудь в строке поиска')