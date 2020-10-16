from django.contrib import admin
from . models import Equipment_SI, Equipment_IO, Equipment_VO, Equipment_SM, Equipment_OP, Equipment_VOA, Equipment_VU, Equipment_SPI
from . models import Equip_SI_part, Equip_IO_part, Equip_VO_part, Equip_VOA_part
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

# Register your models here.


class Equipment_SIResource(resources.ModelResource):
    name_of_equipment = Field(attribute='name_of_equipment', column_name='Наименование оборудования')
    model_type = Field(attribute='model_type', column_name='Модель, тип')
    number_gosreestr = Field(attribute='number_gosreestr', column_name='Номер в госреестре СИ')
    po = Field(attribute='po', column_name='Программное обеспечение')
    company = Field(attribute='company', column_name='Наименование компании производителя')
    factury_number = Field(attribute='factury_number', column_name='Заводской Номер:')
    invent_number = Field(attribute='invent_number', column_name='Инвентарный номер')
    main_document = Field(attribute='main_document', column_name='Наименование, шифр эксплуатационного документа')
    date_manufactur = Field(attribute='date_manufactur', column_name='Дата изготовления')
    date_start_usage = Field(attribute='date_start_usage', column_name='Дата ввода в эксплуатацию')
    location_lab = Field(attribute='location_lab', column_name='Место нахождения')
    microclimate = Field(attribute='microclimate', column_name='Условия эксплуатации')
    range_of_measure = Field(attribute='range_of_measure', column_name='Предел (диапазон) измерений')
    class_measure = Field(attribute='class_measure', column_name='Класс точности, погрешность')
    organization_check = Field(attribute='organization_check', column_name='Организация, выполнившая поверку СИ')
    range_check = Field(attribute='range_check', column_name='Периодичность поверки СИ, мес')
    last_verification = Field(attribute='last_verification', column_name='Поверка СИ')
    last_maintaince = Field(attribute='last_maintaince', column_name='Техническое обслуживание, ремонт')
    tech_condition = Field(attribute='tech_condition', column_name='Техническое состояние')
    responsible_for_use = Field(attribute='responsible_for_use', column_name='Должность, инициалы, фамилия ответственного за эксплуатацию оборудования')
    fact = Field(attribute='fact', column_name='Примечание')

    class Meta:
        model = Equipment_SI
        skip_unchanged = True
        report_skipped = True

class EquipmentSIAdmin(ImportExportModelAdmin):
    resource_class = Equipment_SIResource


class Equipment_IOResource(resources.ModelResource):
    name_of_equipment = Field(attribute='name_of_equipment', column_name='Наименование оборудования')
    model_type = Field(attribute='model_type', column_name='Модель, тип')
    po = Field(attribute='po', column_name='Программное обеспечение')
    company = Field(attribute='company', column_name='Наименование компании производителя')
    factury_number = Field(attribute='factury_number', column_name='Заводской Номер:')
    invent_number = Field(attribute='invent_number', column_name='Инвентарный номер')
    main_document = Field(attribute='main_document', column_name='Наименование, шифр эксплуатационного документа')
    date_manufactur = Field(attribute='date_manufactur', column_name='Дата изготовления')
    date_get=Field(attribute='date_get', column_name='Дата получения')
    date_start_usage = Field(attribute='date_start_usage', column_name='Дата ввода в эксплуатацию')
    location_lab = Field(attribute='location_lab', column_name='Место нахождения')
    microclimate = Field(attribute='microclimate', column_name='Условия эксплуатации')
    organization_check = Field(attribute='organization_check', column_name='Организация, выполнившая аттестацию ИО')
    range_check = Field(attribute='range_check', column_name='Периодичность Аттестации, мес')
    last_verification = Field(attribute='last_verification', column_name='Аттестация ИО')
    last_maintaince = Field(attribute='last_maintaince', column_name='Техническое обслуживание, ремонт')
    tech_condition = Field(attribute='tech_condition', column_name='Техническое состояние')
    responsible_for_use = Field(attribute='responsible_for_use', column_name='Должность, инициалы, фамилия ответственного за эксплуатацию оборудования')
    fact = Field(attribute='fact', column_name='Примечание')

    class Meta:
        model = Equipment_IO
        skip_unchanged = True
        report_skipped = True

class EquipmentIOAdmin(ImportExportModelAdmin):
    resource_class = Equipment_IOResource


class Equipment_VOResource(resources.ModelResource):
    name_of_equipment = Field(attribute='name_of_equipment', column_name='Наименование оборудования')
    model_type = Field(attribute='model_type', column_name='Модель, тип')
    po = Field(attribute='po', column_name='Программное обеспечение')
    company = Field(attribute='company', column_name='Наименование компании производителя')
    factury_number = Field(attribute='factury_number', column_name='Заводской Номер:')
    invent_number = Field(attribute='invent_number', column_name='Инвентарный номер')
    pasport_cto=Field(attribute='pasport_cto', column_name='Паспорт по 174-2011 (дата утверждения)')
    main_document = Field(attribute='main_document', column_name='Наименование, шифр эксплуатационного документа')
    date_manufactur = Field(attribute='date_manufactur', column_name='Дата изготовления')
    date_start_usage = Field(attribute='date_start_usage', column_name='Дата ввода в эксплуатацию')
    location_lab = Field(attribute='location_lab', column_name='Место нахождения')
    microclimate = Field(attribute='microclimate', column_name='Условия эксплуатации')
    last_maintaince = Field(attribute='last_maintaince', column_name='Техническое обслуживание, ремонт')
    tech_condition = Field(attribute='tech_condition', column_name='Техническое состояние')
    responsible_for_use = Field(attribute='responsible_for_use', column_name='Должность, инициалы, фамилия ответственного за эксплуатацию оборудования')
    fact = Field(attribute='fact', column_name='Примечание')

    class Meta:
        model = Equipment_VO
        skip_unchanged = True
        report_skipped = True

class EquipmentVOAdmin(ImportExportModelAdmin):
    resource_class = Equipment_VOResource


class Equipment_SMResource(resources.ModelResource):
    name_of_equipment = Field(attribute='name_of_equipment', column_name='Наименование оборудования')
    model_type = Field(attribute='model_type', column_name='Модель, тип')
    number_gosreestr = Field(attribute='number_gosreestr', column_name='Номер в госреестре СИ')
    po = Field(attribute='po', column_name='Программное обеспечение')
    company = Field(attribute='company', column_name='Наименование компании производителя')
    factury_number = Field(attribute='factury_number', column_name='Заводской Номер:')
    invent_number = Field(attribute='invent_number', column_name='Инвентарный номер')
    main_document = Field(attribute='main_document', column_name='Наименование, шифр эксплуатационного документа')
    date_manufactur = Field(attribute='date_manufactur', column_name='Дата изготовления')
    date_start_usage = Field(attribute='date_start_usage', column_name='Дата ввода в эксплуатацию')
    location_lab = Field(attribute='location_lab', column_name='Место нахождения')
    microclimate = Field(attribute='microclimate', column_name='Условия эксплуатации')
    range_of_measure = Field(attribute='range_of_measure', column_name='Предел (диапазон) измерений')
    class_measure = Field(attribute='class_measure', column_name='Класс точности, погрешность')
    organization_check = Field(attribute='organization_check', column_name='Организация, выполнившая поверку СИ')
    range_check = Field(attribute='range_check', column_name='Периодичность поверки СИ, мес')
    last_verification = Field(attribute='last_verification', column_name='Поверка СИ')
    last_maintaince = Field(attribute='last_maintaince', column_name='Техническое обслуживание, ремонт')
    tech_condition = Field(attribute='tech_condition', column_name='Техническое состояние')
    responsible_for_use = Field(attribute='responsible_for_use', column_name='Должность, инициалы, фамилия ответственного за эксплуатацию оборудования')
    fact = Field(attribute='fact', column_name='Примечание')

    class Meta:
        model = Equipment_SM
        skip_unchanged = True
        report_skipped = True

class EquipmentSMAdmin(ImportExportModelAdmin):
    resource_class = Equipment_SMResource


class Equipment_OPResource(resources.ModelResource):
    name_of_equipment = Field(attribute='name_of_equipment', column_name='Наименование оборудования')
    name_as_passport = Field(attribute='name_as_passport', column_name='Наименование по паспорту')
    model_type = Field(attribute='model_type', column_name='Модель, тип')
    number_gosreestr = Field(attribute='number_gosreestr', column_name='Номер в госреестре СИ')
    po = Field(attribute='po', column_name='Программное обеспечение')
    company = Field(attribute='company', column_name='Наименование компании производителя')
    pasport_cto=Field(attribute='pasport_cto', column_name='Паспорт по 174-2011 (дата утверждения)')
    factury_number = Field(attribute='factury_number', column_name='Заводской Номер:')
    invent_number = Field(attribute='invent_number', column_name='Инвентарный номер')
    main_document = Field(attribute='main_document', column_name='Наименование, шифр эксплуатационного документа')
    date_get=Field(attribute='date_get', column_name='Дата получения')
    date_start_usage = Field(attribute='date_start_usage', column_name='Дата ввода в эксплуатацию')
    location_lab = Field(attribute='location_lab', column_name='Место нахождения')
    microclimate = Field(attribute='microclimate', column_name='Условия эксплуатации')
    responsible_for_use = Field(attribute='responsible_for_use', column_name='Должность, инициалы, фамилия ответственного за эксплуатацию оборудования')
    fact = Field(attribute='fact', column_name='Примечание')

    class Meta:
        model = Equipment_OP
        skip_unchanged = True
        report_skipped = True

class EquipmentOPAdmin(ImportExportModelAdmin):
    resource_class = Equipment_OPResource


# Оборудование вне области аккредитации

class Equipment_VOAResource(resources.ModelResource):
    name_of_equipment = Field(attribute='name_of_equipment', column_name='Наименование оборудования')
    model_type = Field(attribute='model_type', column_name='Модель, тип')
    number_gosreestr = Field(attribute='number_gosreestr', column_name='Номер в госреестре СИ')
    po = Field(attribute='po', column_name='Программное обеспечение')
    company = Field(attribute='company', column_name='Наименование компании производителя')
    factury_number = Field(attribute='factury_number', column_name='Заводской Номер:')
    invent_number = Field(attribute='invent_number', column_name='Инвентарный номер')
    main_document = Field(attribute='main_document', column_name='Наименование, шифр эксплуатационного документа')
    date_manufactur = Field(attribute='date_manufactur', column_name='Дата изготовления')
    date_start_usage = Field(attribute='date_start_usage', column_name='Дата ввода в эксплуатацию')
    location_lab = Field(attribute='location_lab', column_name='Место нахождения')
    microclimate = Field(attribute='microclimate', column_name='Условия эксплуатации')
    range_of_measure = Field(attribute='range_of_measure', column_name='Предел (диапазон) измерений')
    class_measure = Field(attribute='class_measure', column_name='Класс точности, погрешность')
    organization_check = Field(attribute='organization_check', column_name='Организация, выполнившая поверку, калибровку СИ')
    range_check = Field(attribute='range_check', column_name='Периодичность поверки, калибровки СИ, мес')
    last_verification = Field(attribute='last_verification', column_name='Поверка, аттестация ИО')
    last_maintaince = Field(attribute='last_maintaince', column_name='Техническое обслуживание, ремонт')
    tech_condition = Field(attribute='tech_condition', column_name='Техническое состояние')
    responsible_for_use = Field(attribute='responsible_for_use', column_name='Должность, инициалы, фамилия ответственного за эксплуатацию оборудования')
    fact = Field(attribute='fact', column_name='Примечание')

    class Meta:
        model = Equipment_VOA
        skip_unchanged = True
        report_skipped = True

class EquipmentVOAAdmin(ImportExportModelAdmin):
    resource_class = Equipment_VOAResource

# Оборудование выведенное из эксплуатации

class Equipment_VUResource(resources.ModelResource):
    name_of_equipment = Field(attribute='name_of_equipment', column_name='Наименование оборудования')
    model_type = Field(attribute='model_type', column_name='Модель, тип')
    company = Field(attribute='company', column_name='Наименование компании производителя')
    factury_number = Field(attribute='factury_number', column_name='Заводской Номер:')
    invent_number = Field(attribute='invent_number', column_name='Инвентарный номер')
    date_manufactur = Field(attribute='date_manufactur', column_name='Дата изготовления')
    date_start_usage = Field(attribute='date_start_usage', column_name='Дата ввода в эксплуатацию')
    location_lab = Field(attribute='location_lab', column_name='Место нахождения')
    date_end_usage = Field(attribute='date_end_usage', column_name='Дата вывода из эксплуатации')
    reason_of_out = Field(attribute='reason_of_out', column_name='Причина вывода из эксплуатации')
    fact = Field(attribute='fact', column_name='Примечание')

    class Meta:
        model = Equipment_VU
        skip_unchanged = True
        report_skipped = True

class EquipmentVUAdmin(ImportExportModelAdmin):
    resource_class = Equipment_VUResource



# Списанное лабораторное оборудование
class Equipment_SPIResource(resources.ModelResource):
    name_of_equipment = Field(attribute='name_of_equipment', column_name='Наименование оборудования')
    model_type = Field(attribute='model_type', column_name='Модель, тип')
    company = Field(attribute='company', column_name='Наименование компании производителя')
    factury_number = Field(attribute='factury_number', column_name='Заводской Номер:')
    invent_number = Field(attribute='invent_number', column_name='Инвентарный номер')
    date_manufactur = Field(attribute='date_manufactur', column_name='Дата изготовления')
    date_start_usage = Field(attribute='date_start_usage', column_name='Дата ввода в эксплуатацию')
    location_lab = Field(attribute='location_lab', column_name='Место нахождения')
    date_end_usage = Field(attribute='date_end_usage', column_name='Дата вывода из эксплуатации')
    reason_of_out = Field(attribute='reason_of_out', column_name='Причина вывода из эксплуатации')
    fact = Field(attribute='fact', column_name='Примечание')

    class Meta:
        model = Equipment_SPI
        skip_unchanged = True
        report_skipped = True

class EquipmentSPIAdmin(ImportExportModelAdmin):
    resource_class = Equipment_SPIResource

admin.site.register(Equipment_SI, EquipmentSIAdmin)
admin.site.register(Equipment_IO, EquipmentIOAdmin)
admin.site.register(Equipment_VO, EquipmentVOAdmin)
admin.site.register(Equipment_SM, EquipmentSMAdmin)
admin.site.register(Equipment_OP, EquipmentOPAdmin)
admin.site.register(Equipment_VOA, EquipmentVOAAdmin)
admin.site.register(Equipment_VU, EquipmentVUAdmin)
admin.site.register(Equipment_SPI, EquipmentSPIAdmin)


#запчасти и расходные материалы
admin.site.register(Equip_SI_part)
admin.site.register(Equip_IO_part)
admin.site.register(Equip_VO_part)
admin.site.register(Equip_VOA_part)
