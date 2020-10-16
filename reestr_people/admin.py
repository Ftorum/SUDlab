from django.contrib import admin
from . models import OMVOiG_reestr, OMFF_reestr,OMVS_reestr,OHTI_reestr, OMOIR_reestr,ORIMP_reestr,PO_reestr,RUK_reestr
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

class OMVOiG_reestrResource(resources.ModelResource):
    fio=Field(attribute='fio', column_name='Фамилия, имя, отчество')
    job_description=Field(attribute='job_description', column_name='Должность')
    date_settling=Field(attribute='date_settling', column_name='Дата трудоустройства')
    dogovor=Field(attribute='dogovor', column_name='Основание для привлечения личного труда')
    responsibility=Field(attribute='responsibility', column_name='Выполняемые функции, проводые исследования')
    education=Field(attribute='education', column_name='Образование')
    experience=Field(attribute='experience', column_name='Опыт работы')
    attestation_date_protocol=Field(attribute='attestation_date_protocol', column_name='Дата и номер протокола аттестации, периодичность аттестации')
    qualification_up=Field(attribute='qualification_up', column_name='Сведения о повышении квалификации')
    date_job_describ=Field(attribute='date_job_describ', column_name='Дата утверждения должностной инструкции')
    information=Field(attribute='information', column_name='Примечание')
    class Meta:
        model = OMVOiG_reestr
        skip_unchanged = True
        report_skipped = True

class OMVOiG_reestrAdmin(ImportExportModelAdmin):
    resource_class = OMVOiG_reestrResource




class OMFF_reestrResource(resources.ModelResource):
    fio=Field(attribute='fio', column_name='Фамилия, имя, отчество')
    job_description=Field(attribute='job_description', column_name='Должность')
    date_settling=Field(attribute='date_settling', column_name='Дата трудоустройства')
    dogovor=Field(attribute='dogovor', column_name='Основание для привлечения личного труда')
    responsibility=Field(attribute='responsibility', column_name='Выполняемые функции, проводые исследования')
    education=Field(attribute='education', column_name='Образование')
    experience=Field(attribute='experience', column_name='Опыт работы')
    attestation_date_protocol=Field(attribute='attestation_date_protocol', column_name='Дата и номер протокола аттестации, периодичность аттестации')
    qualification_up=Field(attribute='qualification_up', column_name='Сведения о повышении квалификации')
    date_job_describ=Field(attribute='date_job_describ', column_name='Дата утверждения должностной инструкции')
    information=Field(attribute='information', column_name='Примечание')
    class Meta:
        model = OMFF_reestr
        skip_unchanged = True
        report_skipped = True

class OMFF_reestrAdmin(ImportExportModelAdmin):
    resource_class = OMFF_reestrResource




class OMVS_reestrResource(resources.ModelResource):
    fio=Field(attribute='fio', column_name='Фамилия, имя, отчество')
    job_description=Field(attribute='job_description', column_name='Должность')
    date_settling=Field(attribute='date_settling', column_name='Дата трудоустройства')
    dogovor=Field(attribute='dogovor', column_name='Основание для привлечения личного труда')
    responsibility=Field(attribute='responsibility', column_name='Выполняемые функции, проводые исследования')
    education=Field(attribute='education', column_name='Образование')
    experience=Field(attribute='experience', column_name='Опыт работы')
    attestation_date_protocol=Field(attribute='attestation_date_protocol', column_name='Дата и номер протокола аттестации, периодичность аттестации')
    qualification_up=Field(attribute='qualification_up', column_name='Сведения о повышении квалификации')
    date_job_describ=Field(attribute='date_job_describ', column_name='Дата утверждения должностной инструкции')
    information=Field(attribute='information', column_name='Примечание')
    class Meta:
        model = OMVS_reestr
        skip_unchanged = True
        report_skipped = True

class OMVS_reestrAdmin(ImportExportModelAdmin):
    resource_class = OMVS_reestrResource




class OHTI_reestrResource(resources.ModelResource):
    fio=Field(attribute='fio', column_name='Фамилия, имя, отчество')
    job_description=Field(attribute='job_description', column_name='Должность')
    date_settling=Field(attribute='date_settling', column_name='Дата трудоустройства')
    dogovor=Field(attribute='dogovor', column_name='Основание для привлечения личного труда')
    responsibility=Field(attribute='responsibility', column_name='Выполняемые функции, проводые исследования')
    education=Field(attribute='education', column_name='Образование')
    experience=Field(attribute='experience', column_name='Опыт работы')
    attestation_date_protocol=Field(attribute='attestation_date_protocol', column_name='Дата и номер протокола аттестации, периодичность аттестации')
    qualification_up=Field(attribute='qualification_up', column_name='Сведения о повышении квалификации')
    date_job_describ=Field(attribute='date_job_describ', column_name='Дата утверждения должностной инструкции')
    information=Field(attribute='information', column_name='Примечание')
    class Meta:
        model = OHTI_reestr
        skip_unchanged = True
        report_skipped = True

class OHTI_reestrAdmin(ImportExportModelAdmin):
    resource_class = OHTI_reestrResource
 


class OMOIR_reestrResource(resources.ModelResource):
    fio=Field(attribute='fio', column_name='Фамилия, имя, отчество')
    job_description=Field(attribute='job_description', column_name='Должность')
    date_settling=Field(attribute='date_settling', column_name='Дата трудоустройства')
    dogovor=Field(attribute='dogovor', column_name='Основание для привлечения личного труда')
    responsibility=Field(attribute='responsibility', column_name='Выполняемые функции, проводые исследования')
    education=Field(attribute='education', column_name='Образование')
    experience=Field(attribute='experience', column_name='Опыт работы')
    attestation_date_protocol=Field(attribute='attestation_date_protocol', column_name='Дата и номер протокола аттестации, периодичность аттестации')
    qualification_up=Field(attribute='qualification_up', column_name='Сведения о повышении квалификации')
    date_job_describ=Field(attribute='date_job_describ', column_name='Дата утверждения должностной инструкции')
    information=Field(attribute='information', column_name='Примечание')
    class Meta:
        model = OMOIR_reestr
        skip_unchanged = True
        report_skipped = True

class OMOIR_reestrAdmin(ImportExportModelAdmin):
    resource_class = OMOIR_reestrResource


class ORIMP_reestrResource(resources.ModelResource):
    fio=Field(attribute='fio', column_name='Фамилия, имя, отчество')
    job_description=Field(attribute='job_description', column_name='Должность')
    date_settling=Field(attribute='date_settling', column_name='Дата трудоустройства')
    dogovor=Field(attribute='dogovor', column_name='Основание для привлечения личного труда')
    responsibility=Field(attribute='responsibility', column_name='Выполняемые функции, проводые исследования')
    education=Field(attribute='education', column_name='Образование')
    experience=Field(attribute='experience', column_name='Опыт работы')
    attestation_date_protocol=Field(attribute='attestation_date_protocol', column_name='Дата и номер протокола аттестации, периодичность аттестации')
    qualification_up=Field(attribute='qualification_up', column_name='Сведения о повышении квалификации')
    date_job_describ=Field(attribute='date_job_describ', column_name='Дата утверждения должностной инструкции')
    information=Field(attribute='information', column_name='Примечание')
    class Meta:
        model = ORIMP_reestr
        skip_unchanged = True
        report_skipped = True

class ORIMP_reestrAdmin(ImportExportModelAdmin):
    resource_class = ORIMP_reestrResource





class PO_reestrResource(resources.ModelResource):
    fio=Field(attribute='fio', column_name='Фамилия, имя, отчество')
    job_description=Field(attribute='job_description', column_name='Должность')
    date_settling=Field(attribute='date_settling', column_name='Дата трудоустройства')
    dogovor=Field(attribute='dogovor', column_name='Основание для привлечения личного труда')
    responsibility=Field(attribute='responsibility', column_name='Выполняемые функции, проводые исследования')
    education=Field(attribute='education', column_name='Образование')
    experience=Field(attribute='experience', column_name='Опыт работы')
    attestation_date_protocol=Field(attribute='attestation_date_protocol', column_name='Дата и номер протокола аттестации, периодичность аттестации')
    qualification_up=Field(attribute='qualification_up', column_name='Сведения о повышении квалификации')
    date_job_describ=Field(attribute='date_job_describ', column_name='Дата утверждения должностной инструкции')
    information=Field(attribute='information', column_name='Примечание')
    class Meta:
        model = PO_reestr
        skip_unchanged = True
        report_skipped = True

class PO_reestrAdmin(ImportExportModelAdmin):
    resource_class = PO_reestrResource



class RUK_reestrResource(resources.ModelResource):
    fio=Field(attribute='fio', column_name='Фамилия, имя, отчество')
    job_description=Field(attribute='job_description', column_name='Должность')
    date_settling=Field(attribute='date_settling', column_name='Дата трудоустройства')
    dogovor=Field(attribute='dogovor', column_name='Основание для привлечения личного труда')
    responsibility=Field(attribute='responsibility', column_name='Выполняемые функции, проводые исследования')
    education=Field(attribute='education', column_name='Образование')
    experience=Field(attribute='experience', column_name='Опыт работы')
    attestation_date_protocol=Field(attribute='attestation_date_protocol', column_name='Дата и номер протокола аттестации, периодичность аттестации')
    qualification_up=Field(attribute='qualification_up', column_name='Сведения о повышении квалификации')
    date_job_describ=Field(attribute='date_job_describ', column_name='Дата утверждения должностной инструкции')
    information=Field(attribute='information', column_name='Примечание')
    class Meta:
        model = PO_reestr
        skip_unchanged = True
        report_skipped = True

class RUK_reestrAdmin(ImportExportModelAdmin):
    resource_class = RUK_reestrResource







# Register your models here.
admin.site.register(OMVOiG_reestr, OMVOiG_reestrAdmin)
admin.site.register(OMFF_reestr, OMFF_reestrAdmin)
admin.site.register(OMVS_reestr, OMVS_reestrAdmin)
admin.site.register(OHTI_reestr, OHTI_reestrAdmin)
admin.site.register(OMOIR_reestr, OMOIR_reestrAdmin)
admin.site.register(ORIMP_reestr, ORIMP_reestrAdmin)
admin.site.register(PO_reestr, PO_reestrAdmin)
admin.site.register(RUK_reestr, RUK_reestrAdmin)



