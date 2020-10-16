from django.contrib import admin
from . models import Equipment_SI_OMVS, Equipment_IO_OMVS, Equipment_VO_OMVS, Equipment_SM_OMVS, Equipment_OP_OMVS, Equipment_VOA_OMVS, Equipment_VU_OMVS, Equipment_SPI_OMVS
from . models import Equip_SI_part_OMVS, Equip_IO_part_OMVS, Equip_VO_part_OMVS, Equip_VOA_part_OMVS
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

# Register your models here.


class Equipment_SI_OMVSResource(resources.ModelResource):
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
        model = Equipment_SI_OMVS
        skip_unchanged = True
        report_skipped = True

class EquipmentSI_OMVSAdmin(ImportExportModelAdmin):
    resource_class = Equipment_SI_OMVSResource


class Equipment_IO_OMVSResource(resources.ModelResource):
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
        model = Equipment_IO_OMVS
        skip_unchanged = True
        report_skipped = True

class EquipmentIO_OMVSAdmin(ImportExportModelAdmin):
    resource_class = Equipment_IO_OMVSResource


class Equipment_VO_OMVSResource(resources.ModelResource):
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
        model = Equipment_VO_OMVS
        skip_unchanged = True
        report_skipped = True

class EquipmentVO_OMVSAdmin(ImportExportModelAdmin):
    resource_class = Equipment_VO_OMVSResource


class Equipment_SM_OMVSResource(resources.ModelResource):
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
        model = Equipment_SM_OMVS
        skip_unchanged = True
        report_skipped = True

class EquipmentSM_OMVSAdmin(ImportExportModelAdmin):
    resource_class = Equipment_SM_OMVSResource


class Equipment_OP_OMVSResource(resources.ModelResource):
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
        model = Equipment_OP_OMVS
        skip_unchanged = True
        report_skipped = True

class EquipmentOP_OMVSAdmin(ImportExportModelAdmin):
    resource_class = Equipment_OP_OMVSResource


# Оборудование вне области аккредитации

class Equipment_VOA_OMVSResource(resources.ModelResource):
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
        model = Equipment_VOA_OMVS
        skip_unchanged = True
        report_skipped = True

class EquipmentVOA_OMVSAdmin(ImportExportModelAdmin):
    resource_class = Equipment_VOA_OMVSResource

# Оборудование выведенное из эксплуатации

class Equipment_VU_OMVSResource(resources.ModelResource):
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
        model = Equipment_VU_OMVS
        skip_unchanged = True
        report_skipped = True

class EquipmentVU_OMVSAdmin(ImportExportModelAdmin):
    resource_class = Equipment_VU_OMVSResource



# Списанное лабораторное оборудование
class Equipment_SPI_OMVSResource(resources.ModelResource):
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
        model = Equipment_SPI_OMVS
        skip_unchanged = True
        report_skipped = True

class EquipmentSPI_OMVSAdmin(ImportExportModelAdmin):
    resource_class = Equipment_SPI_OMVSResource

admin.site.register(Equipment_SI_OMVS, EquipmentSI_OMVSAdmin)
admin.site.register(Equipment_IO_OMVS, EquipmentIO_OMVSAdmin)
admin.site.register(Equipment_VO_OMVS, EquipmentVO_OMVSAdmin)
admin.site.register(Equipment_SM_OMVS, EquipmentSM_OMVSAdmin)
admin.site.register(Equipment_OP_OMVS, EquipmentOP_OMVSAdmin)
admin.site.register(Equipment_VOA_OMVS, EquipmentVOA_OMVSAdmin)
admin.site.register(Equipment_VU_OMVS, EquipmentVU_OMVSAdmin)
admin.site.register(Equipment_SPI_OMVS, EquipmentSPI_OMVSAdmin)


#запчасти и расходные материалы
admin.site.register(Equip_SI_part_OMVS)
admin.site.register(Equip_IO_part_OMVS)
admin.site.register(Equip_VO_part_OMVS)
admin.site.register(Equip_VOA_part_OMVS)
# Register your models here.
