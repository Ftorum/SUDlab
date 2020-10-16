from django.contrib import admin
from . models import Equipment_SI_OHTI, Equipment_IO_OHTI, Equipment_VO_OHTI, Equipment_SM_OHTI, Equipment_OP_OHTI, Equipment_VOA_OHTI, Equipment_VU_OHTI, Equipment_SPI_OHTI
from . models import Equip_SI_part_OHTI, Equip_IO_part_OHTI, Equip_VO_part_OHTI, Equip_VOA_part_OHTI
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

# Register your models here.


class Equipment_SI_OHTIResource(resources.ModelResource):
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
        model = Equipment_SI_OHTI
        skip_unchanged = True
        report_skipped = True

class EquipmentSI_OHTIAdmin(ImportExportModelAdmin):
    resource_class = Equipment_SI_OHTIResource


class Equipment_IO_OHTIResource(resources.ModelResource):
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
        model = Equipment_IO_OHTI
        skip_unchanged = True
        report_skipped = True

class EquipmentIO_OHTIAdmin(ImportExportModelAdmin):
    resource_class = Equipment_IO_OHTIResource


class Equipment_VO_OHTIResource(resources.ModelResource):
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
        model = Equipment_VO_OHTI
        skip_unchanged = True
        report_skipped = True

class EquipmentVO_OHTIAdmin(ImportExportModelAdmin):
    resource_class = Equipment_VO_OHTIResource


class Equipment_SM_OHTIResource(resources.ModelResource):
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
        model = Equipment_SM_OHTI
        skip_unchanged = True
        report_skipped = True

class EquipmentSM_OHTIAdmin(ImportExportModelAdmin):
    resource_class = Equipment_SM_OHTIResource


class Equipment_OP_OHTIResource(resources.ModelResource):
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
        model = Equipment_OP_OHTI
        skip_unchanged = True
        report_skipped = True

class EquipmentOP_OHTIAdmin(ImportExportModelAdmin):
    resource_class = Equipment_OP_OHTIResource


# Оборудование вне области аккредитации

class Equipment_VOA_OHTIResource(resources.ModelResource):
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
        model = Equipment_VOA_OHTI
        skip_unchanged = True
        report_skipped = True

class EquipmentVOA_OHTIAdmin(ImportExportModelAdmin):
    resource_class = Equipment_VOA_OHTIResource

# Оборудование выведенное из эксплуатации

class Equipment_VU_OHTIResource(resources.ModelResource):
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
        model = Equipment_VU_OHTI
        skip_unchanged = True
        report_skipped = True

class EquipmentVU_OHTIAdmin(ImportExportModelAdmin):
    resource_class = Equipment_VU_OHTIResource



# Списанное лабораторное оборудование
class Equipment_SPI_OHTIResource(resources.ModelResource):
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
        model = Equipment_SPI_OHTI
        skip_unchanged = True
        report_skipped = True

class EquipmentSPI_OHTIAdmin(ImportExportModelAdmin):
    resource_class = Equipment_SPI_OHTIResource

admin.site.register(Equipment_SI_OHTI, EquipmentSI_OHTIAdmin)
admin.site.register(Equipment_IO_OHTI, EquipmentIO_OHTIAdmin)
admin.site.register(Equipment_VO_OHTI, EquipmentVO_OHTIAdmin)
admin.site.register(Equipment_SM_OHTI, EquipmentSM_OHTIAdmin)
admin.site.register(Equipment_OP_OHTI, EquipmentOP_OHTIAdmin)
admin.site.register(Equipment_VOA_OHTI, EquipmentVOA_OHTIAdmin)
admin.site.register(Equipment_VU_OHTI, EquipmentVU_OHTIAdmin)
admin.site.register(Equipment_SPI_OHTI, EquipmentSPI_OHTIAdmin)


#запчасти и расходные материалы
admin.site.register(Equip_SI_part_OHTI)
admin.site.register(Equip_IO_part_OHTI)
admin.site.register(Equip_VO_part_OHTI)
admin.site.register(Equip_VOA_part_OHTI)
# Register your models here.
