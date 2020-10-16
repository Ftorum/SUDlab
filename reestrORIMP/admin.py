from django.contrib import admin
from . models import Equipment_SI_ORIMP, Equipment_IO_ORIMP, Equipment_VO_ORIMP, Equipment_ET_ORIMP, Equipment_RET_ORIMP
from . models import Equip_SI_part_ORIMP, Equip_IO_part_ORIMP, Equip_VO_part_ORIMP
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

# Register your models here.
class Equipment_SI_ORIMPResource(resources.ModelResource):
    name_of_equipment_passport = Field(attribute='name_of_equipment_passport', column_name='Наименование оборудования по паспорту')
    name_of_equipment_gos_reestr = Field(attribute='name_of_equipment_gos_reestr', column_name='Наименование оборудования по госреестру')
    equip_R3 = Field(attribute='equip_R3', column_name='Наименование оборудования R3')
    model_type = Field(attribute='model_type', column_name='Модель, тип')
    number_gosreestr = Field(attribute='number_gosreestr', column_name='Номер в госреестре СИ')
    number_etalon = Field(attribute='number_etalon', column_name='Регистрационный номер эталона')
    po = Field(attribute='po', column_name='Программное обеспечение')
    company = Field(attribute='company', column_name='Наименование компании производителя')
    factury_number = Field(attribute='factury_number', column_name='Заводской Номер')
    invent_number = Field(attribute='invent_number', column_name='Инвентарный номер')
    main_document = Field(attribute='main_document', column_name='Наименование, шифр эксплуатационного документа')
    range_of_measure = Field(attribute='range_of_measure', column_name='Предел (диапазон) измерений')
    class_measure = Field(attribute='class_measure', column_name='Класс точности, погрешность')
    location_lab = Field(attribute='location_lab', column_name='Место нахождения (кабинет)')
    microclimate = Field(attribute='microclimate', column_name='Условия эксплуатации')
    organization_check = Field(attribute='organization_check', column_name='Организация, выполнившая поверку СИ')
    range_check = Field(attribute='range_check', column_name='Переодичность поверки(мес)')
    last_verification = Field(attribute='last_verification', column_name='Поверка СИ')
    next_verification = Field(attribute='next_verification', column_name='Дата следующей поверки/калибровки/аттестации')
    last_maintaince = Field(attribute='last_maintaince', column_name='Техническое обслужинание, ремонт')
    tech_condition = Field(attribute='tech_condition', column_name='Техническое состояние')
    date_manufactur = Field(attribute='date_manufactur', column_name='Дата изготовления')
    date_start_usage = Field(attribute='date_start_usage', column_name='Дата ввода в эксплуатацию')
    fact = Field(attribute='fact', column_name='Примечание')

    class Meta:
        model = Equipment_SI_ORIMP
        skip_unchanged = True
        report_skipped = True

class EquipmentSI_ORIMPAdmin(ImportExportModelAdmin):
    resource_class = Equipment_SI_ORIMPResource



class Equipment_IO_ORIMPResource(resources.ModelResource):
    name_of_equipment_passport = Field(attribute='name_of_equipment_passport', column_name='Наименование оборудования по паспорту')
    name_of_equipment_gos_reestr = Field(attribute='name_of_equipment_gos_reestr', column_name='Наименование оборудования по госреестру')
    equip_R3 = Field(attribute='equip_R3', column_name='Наименование оборудования R3')
    model_type = Field(attribute='model_type', column_name='Модель, тип')
    number_gosreestr = Field(attribute='number_gosreestr', column_name='Номер в госреестре СИ')
    number_etalon = Field(attribute='number_etalon', column_name='Регистрационный номер эталона')
    po = Field(attribute='po', column_name='Программное обеспечение')
    company = Field(attribute='company', column_name='Наименование компании производителя')
    factury_number = Field(attribute='factury_number', column_name='Заводской Номер')
    invent_number = Field(attribute='invent_number', column_name='Инвентарный номер')
    main_document = Field(attribute='main_document', column_name='Наименование, шифр эксплуатационного документа')
    range_of_measure = Field(attribute='range_of_measure', column_name='Предел (диапазон) измерений')
    class_measure = Field(attribute='class_measure', column_name='Класс точности, погрешность')
    location_lab = Field(attribute='location_lab', column_name='Место нахождения (кабинет)')
    microclimate = Field(attribute='microclimate', column_name='Условия эксплуатации')
    organization_check = Field(attribute='organization_check', column_name='Организация, выполнившая поверку СИ')
    range_check = Field(attribute='range_check', column_name='Переодичность поверки(мес)')
    last_verification = Field(attribute='last_verification', column_name='Поверка СИ')
    next_verification = Field(attribute='next_verification', column_name='Дата следующей поверки/калибровки/аттестации')
    last_maintaince = Field(attribute='last_maintaince', column_name='Техническое обслужинание, ремонт')
    tech_condition = Field(attribute='tech_condition', column_name='Техническое состояние')
    date_manufactur = Field(attribute='date_manufactur', column_name='Дата изготовления')
    date_start_usage = Field(attribute='date_start_usage', column_name='Дата ввода в эксплуатацию')
    fact = Field(attribute='fact', column_name='Примечание')

    class Meta:
        model = Equipment_IO_ORIMP
        skip_unchanged = True
        report_skipped = True

class EquipmentIO_ORIMPAdmin(ImportExportModelAdmin):
    resource_class = Equipment_IO_ORIMPResource


class Equipment_VO_ORIMPResource(resources.ModelResource):
    name_of_equipment_passport = Field(attribute='name_of_equipment_passport', column_name='Наименование оборудования по паспорту')
    name_of_equipment_gos_reestr = Field(attribute='name_of_equipment_gos_reestr', column_name='Наименование оборудования по госреестру')
    equip_R3 = Field(attribute='equip_R3', column_name='Наименование оборудования R3')
    model_type = Field(attribute='model_type', column_name='Модель, тип')
    number_gosreestr = Field(attribute='number_gosreestr', column_name='Номер в госреестре СИ')
    number_etalon = Field(attribute='number_etalon', column_name='Регистрационный номер эталона')
    po = Field(attribute='po', column_name='Программное обеспечение')
    company = Field(attribute='company', column_name='Наименование компании производителя')
    factury_number = Field(attribute='factury_number', column_name='Заводской Номер')
    invent_number = Field(attribute='invent_number', column_name='Инвентарный номер')
    main_document = Field(attribute='main_document', column_name='Наименование, шифр эксплуатационного документа')
    range_of_measure = Field(attribute='range_of_measure', column_name='Предел (диапазон) измерений')
    class_measure = Field(attribute='class_measure', column_name='Класс точности, погрешность')
    location_lab = Field(attribute='location_lab', column_name='Место нахождения (кабинет)')
    microclimate = Field(attribute='microclimate', column_name='Условия эксплуатации')
    organization_check = Field(attribute='organization_check', column_name='Организация, выполнившая поверку СИ')
    range_check = Field(attribute='range_check', column_name='Переодичность поверки(мес)')
    last_verification = Field(attribute='last_verification', column_name='Поверка СИ')
    next_verification = Field(attribute='next_verification', column_name='Дата следующей поверки/калибровки/аттестации')
    last_maintaince = Field(attribute='last_maintaince', column_name='Техническое обслужинание, ремонт')
    tech_condition = Field(attribute='tech_condition', column_name='Техническое состояние')
    date_manufactur = Field(attribute='date_manufactur', column_name='Дата изготовления')
    date_start_usage = Field(attribute='date_start_usage', column_name='Дата ввода в эксплуатацию')
    fact = Field(attribute='fact', column_name='Примечание')

    class Meta:
        model = Equipment_VO_ORIMP
        skip_unchanged = True
        report_skipped = True

class EquipmentVO_ORIMPAdmin(ImportExportModelAdmin):
    resource_class = Equipment_VO_ORIMPResource


class Equipment_ET_ORIMPResource(resources.ModelResource):
    reg_number = Field(attribute='reg_number', column_name='Регистрационный номер эталона')
    name_of_equipment_passport = Field(attribute='name_of_equipment_passport', column_name='Наименование оборудования по паспорту')
    name_of_equipment_measure = Field(attribute='name_of_equipment_measure', column_name='Наименование средств измерений')
    factury_number = Field(attribute='reg_number', column_name='Заводской Номер')
    main_document = Field(attribute='reg_number', column_name='Приказ об утверждени эталонов единиц величин')
    fact = Field(attribute='fact', column_name='Примечание')
    

    class Meta:
        model = Equipment_ET_ORIMP
        skip_unchanged = True
        report_skipped = True

class EquipmentET_ORIMPAdmin(ImportExportModelAdmin):
    resource_class = Equipment_ET_ORIMPResource



class Equipment_RET_ORIMPResource(resources.ModelResource):
    reg_number = Field(attribute='reg_number', column_name='Регистрационный номер эталона')
    name_of_equipment_passport = Field(attribute='name_of_equipment_passport', column_name='Наименование оборудования по паспорту')
    name_of_equipment_measure = Field(attribute='name_of_equipment_measure', column_name='Наименование средств измерений')
    factury_number = Field(attribute='reg_number', column_name='Заводской Номер')
    numb_elect_zayavki = Field(attribute='numb_elect_zayavki', column_name='Номер электронной заявки')
    date_next_verification = Field(attribute='date_next_verification', column_name='Дата следующей поверки')
    date_attestation_et = Field(attribute='date_attestation_et', column_name='Дата аттестации элатона')
    scheme_of_verivication = Field(attribute='scheme_of_verivication', column_name='Наименование Государственной поверочной схемы для средств измерений')
    

    class Meta:
        model = Equipment_RET_ORIMP
        skip_unchanged = True
        report_skipped = True

class EquipmentRET_ORIMPAdmin(ImportExportModelAdmin):
    resource_class = Equipment_RET_ORIMPResource










admin.site.register(Equipment_SI_ORIMP, EquipmentSI_ORIMPAdmin)
admin.site.register(Equipment_IO_ORIMP, EquipmentIO_ORIMPAdmin)
admin.site.register(Equipment_VO_ORIMP, EquipmentVO_ORIMPAdmin)
admin.site.register(Equipment_ET_ORIMP, EquipmentET_ORIMPAdmin)
admin.site.register(Equipment_RET_ORIMP, EquipmentRET_ORIMPAdmin)

#запчасти и расходные материалы
admin.site.register(Equip_SI_part_ORIMP)
admin.site.register(Equip_IO_part_ORIMP)
admin.site.register(Equip_VO_part_ORIMP)
# Register your models here.
