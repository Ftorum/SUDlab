from django.db import models


# Реестр персонала ОМВОиГ.
def directory_path_to_reestr_personal_OMVOIG_img(fio, group): 
    return 'images/OMVOIG/reestr_personal/OMVOiG/{0}/{1}'.format(fio, group) 
class OMVOiG_reestr(models.Model):
    GROUP_CHOICE = ( 
    ("Группа анализа природных и питьевых вод","Группа анализа природных и питьевых вод"), 
    ("Группа хроматографических и спектрометрических исследований","Группа хроматографических и спектрометрических исследований"), 
    ("Группа анализа грунтов","Группа анализа грунтов"),
    ("Группа токсикологических исследований","Группа токсикологических исследований"),
    ("В отделе","В отделе")
    )
    fio=models.CharField('Фамилия, имя, отчество', max_length=250, default='')
    job_description=models.CharField('Должность', max_length=250, default='')
    date_settling=models.DateField('Дата трудоустройства')
    dogovor=models.CharField('Основание для привлечения личного труда', max_length=250, default='')
    responsibility=models.CharField('Выполняемые функции, проводые исследования', max_length=250, default='')
    education=models.CharField('Образование', max_length=250, default='')
    experience=models.CharField('Опыт работы', max_length=250, default='')
    attestation_date_protocol=models.CharField('Дата и номер протокола аттестации, периодичность аттестации', max_length=250, default='')
    qualification_up=models.TextField('Сведения о повышении квалификации', default='-')
    date_job_describ=models.DateField('Дата утверждения должностной инструкции')
    group=models.CharField('Наименование группы', max_length=250, default='',choices = GROUP_CHOICE)
    information=models.CharField('Примечание', max_length=250, default='')
    image_of_person=models.ImageField(null=True,blank=True, upload_to=directory_path_to_reestr_personal_OMVOIG_img)
    def __str__(self):
        return f'{self.fio} : {self.group}'

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Реестр ОМВОиГ'

# Реестр персонала ОМФФ.
def directory_path_to_reestr_personal_OMFF_img(fio, group): 
    return 'images/OMVOIG/reestr_personal/OMFF/{0}/{1}'.format(fio, group) 
class OMFF_reestr(models.Model):
    GROUP_CHOICE = (("Группа радиационного контроля","Группа радиационного контроля"),("В отделе","В отделе"))
    fio=models.CharField('Фамилия, имя, отчество', max_length=250, default='')
    job_description=models.CharField('Должность', max_length=250, default='')
    date_settling=models.DateField('Дата трудоустройства')
    dogovor=models.CharField('Основание для привлечения личного труда', max_length=250, default='')
    responsibility=models.CharField('Выполняемые функции, проводые исследования', max_length=250, default='')
    education=models.CharField('Образование', max_length=250, default='')
    experience=models.CharField('Опыт работы', max_length=250, default='')
    attestation_date_protocol=models.CharField('Дата и номер протокола аттестации, периодичность аттестации', max_length=250, default='')
    qualification_up=models.TextField('Сведения о повышении квалификации', default='-')
    date_job_describ=models.DateField('Дата утверждения должностной инструкции')
    group=models.CharField('Наименование группы', max_length=250, default='-',choices=GROUP_CHOICE)
    information=models.CharField('Примечание', max_length=250, default='')
    image_of_person=models.ImageField(null=True,blank=True, upload_to=directory_path_to_reestr_personal_OMFF_img)
    def __str__(self):
        return f'{self.fio} : {self.group}'

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Реестр ОМФФ'


# Реестр персонала ОМВС
def directory_path_to_reestr_personal_OMVS_img(fio, group): 
    return 'images/OMVOIG/reestr_personal/OMVS/{0}/{1}'.format(fio, group) 
class OMVS_reestr(models.Model):
    GROUP_CHOICE = (
        ("Группа контроля воздуха рабочей зоны","Группа контроля воздуха рабочей зоны"),
        ("Группа по контролю промышленных выбросов и атмосферного воздуха","Группа по контролю промышленных выбросов и атмосферного воздуха"),
        ("В отделе","В отделе"))
    fio=models.CharField('Фамилия, имя, отчество', max_length=250, default='')
    job_description=models.CharField('Должность', max_length=250, default='')
    date_settling=models.DateField('Дата трудоустройства')
    dogovor=models.CharField('Основание для привлечения личного труда', max_length=250, default='')
    responsibility=models.CharField('Выполняемые функции, проводые исследования', max_length=250, default='')
    education=models.CharField('Образование', max_length=250, default='')
    experience=models.CharField('Опыт работы', max_length=250, default='')
    attestation_date_protocol=models.CharField('Дата и номер протокола аттестации, периодичность аттестации', max_length=250, default='')
    qualification_up=models.TextField('Сведения о повышении квалификации', default='-')
    date_job_describ=models.DateField('Дата утверждения должностной инструкции')
    group=models.CharField('Наименование группы', max_length=250, default='-',choices=GROUP_CHOICE)
    information=models.CharField('Примечание', max_length=250, default='')
    image_of_person=models.ImageField(null=True,blank=True, upload_to=directory_path_to_reestr_personal_OMVS_img)
    def __str__(self):
        return f'{self.fio} : {self.group}'

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Реестр ОМВС'

# Реестр персонала ОХТИ
def directory_path_to_reestr_personal_OHTI_img(fio, group): 
    return 'images/OMVOIG/reestr_personal/OHTI/{0}/{1}'.format(fio, group) 
class OHTI_reestr(models.Model):

    fio=models.CharField('Фамилия, имя, отчество', max_length=250, default='')
    job_description=models.CharField('Должность', max_length=250, default='')
    date_settling=models.DateField('Дата трудоустройства')
    dogovor=models.CharField('Основание для привлечения личного труда', max_length=250, default='')
    responsibility=models.CharField('Выполняемые функции, проводые исследования', max_length=250, default='')
    education=models.CharField('Образование', max_length=250, default='')
    experience=models.CharField('Опыт работы', max_length=250, default='')
    attestation_date_protocol=models.CharField('Дата и номер протокола аттестации, периодичность аттестации', max_length=250, default='')
    qualification_up=models.TextField('Сведения о повышении квалификации', default='-')
    date_job_describ=models.DateField('Дата утверждения должностной инструкции')
    information=models.CharField('Примечание', max_length=250, default='')
    image_of_person=models.ImageField(null=True,blank=True, upload_to=directory_path_to_reestr_personal_OHTI_img)
    def __str__(self):
        return f'{self.fio}'

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Реестр ОХТИ'

# Реестр персонала ОМОиР
def directory_path_to_reestr_personal_OMOIR_img(fio, group): 
    return 'images/OMVOIG/reestr_personal/OMOIR/{0}/{1}'.format(fio, group) 
class OMOIR_reestr(models.Model):

    fio=models.CharField('Фамилия, имя, отчество', max_length=250, default='')
    job_description=models.CharField('Должность', max_length=250, default='')
    date_settling=models.DateField('Дата трудоустройства')
    dogovor=models.CharField('Основание для привлечения личного труда', max_length=250, default='')
    responsibility=models.CharField('Выполняемые функции, проводые исследования', max_length=250, default='')
    education=models.CharField('Образование', max_length=250, default='')
    experience=models.CharField('Опыт работы', max_length=250, default='')
    attestation_date_protocol=models.CharField('Дата и номер протокола аттестации, периодичность аттестации', max_length=250, default='')
    qualification_up=models.TextField('Сведения о повышении квалификации', default='-')
    date_job_describ=models.DateField('Дата утверждения должностной инструкции')
    information=models.CharField('Примечание', max_length=250, default='')
    image_of_person=models.ImageField(null=True,blank=True, upload_to=directory_path_to_reestr_personal_OMOIR_img)
    def __str__(self):
        return f'{self.fio}'

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Реестр ОМОиР'

# Реестр персонала ПО
def directory_path_to_reestr_personal_PO_img(fio, group): 
    return 'images/OMVOIG/reestr_personal/PO/{0}/{1}'.format(fio, group) 
class PO_reestr(models.Model):

    fio=models.CharField('Фамилия, имя, отчество', max_length=250, default='')
    job_description=models.CharField('Должность', max_length=250, default='')
    date_settling=models.DateField('Дата трудоустройства')
    dogovor=models.CharField('Основание для привлечения личного труда', max_length=250, default='')
    responsibility=models.CharField('Выполняемые функции, проводые исследования', max_length=250, default='')
    education=models.CharField('Образование', max_length=250, default='')
    experience=models.CharField('Опыт работы', max_length=250, default='')
    attestation_date_protocol=models.CharField('Дата и номер протокола аттестации, периодичность аттестации', max_length=250, default='')
    qualification_up=models.TextField('Сведения о повышении квалификации', default='-')
    date_job_describ=models.DateField('Дата утверждения должностной инструкции')
    information=models.CharField('Примечание', max_length=250, default='')
    image_of_person=models.ImageField(null=True,blank=True, upload_to=directory_path_to_reestr_personal_PO_img)
    def __str__(self):
        return f'{self.fio}'

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Реестр ПO'
    
# Реестр персонала ОРИМР
def directory_path_to_reestr_personal_ORIMP_img(fio, group): 
    return 'images/OMVOIG/reestr_personal/ORIMP/{0}/{1}'.format(fio, group) 
class ORIMP_reestr(models.Model):

    fio=models.CharField('Фамилия, имя, отчество', max_length=250, default='')
    job_description=models.CharField('Должность', max_length=250, default='')
    date_settling=models.DateField('Дата трудоустройства')
    dogovor=models.CharField('Основание для привлечения личного труда', max_length=250, default='')
    responsibility=models.CharField('Выполняемые функции, проводые исследования', max_length=250, default='')
    education=models.CharField('Образование', max_length=250, default='')
    experience=models.CharField('Опыт работы', max_length=250, default='')
    attestation_date_protocol=models.CharField('Дата и номер протокола аттестации, периодичность аттестации', max_length=250, default='')
    qualification_up=models.TextField('Сведения о повышении квалификации', default='-')
    date_job_describ=models.DateField('Дата утверждения должностной инструкции')
    information=models.CharField('Примечание', max_length=250, default='')
    image_of_person=models.ImageField(null=True,blank=True, upload_to=directory_path_to_reestr_personal_ORIMP_img)
    def __str__(self):
        return f'{self.fio}'

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Реестр ОРиМР'

# Реестр персонала Руководство
def directory_path_to_reestr_personal_RUK_img(fio, group): 
    return 'images/OMVOIG/reestr_personal/RUK/{0}/{1}'.format(fio, group) 
class RUK_reestr(models.Model):

    fio=models.CharField('Фамилия, имя, отчество', max_length=250, default='')
    job_description=models.CharField('Должность', max_length=250, default='')
    date_settling=models.DateField('Дата трудоустройства')
    dogovor=models.CharField('Основание для привлечения личного труда', max_length=250, default='')
    responsibility=models.CharField('Выполняемые функции, проводые исследования', max_length=250, default='')
    education=models.CharField('Образование', max_length=250, default='')
    experience=models.CharField('Опыт работы', max_length=250, default='')
    attestation_date_protocol=models.CharField('Дата и номер протокола аттестации, периодичность аттестации', max_length=250, default='')
    qualification_up=models.TextField('Сведения о повышении квалификации', default='-')
    date_job_describ=models.DateField('Дата утверждения должностной инструкции')
    information=models.CharField('Примечание', max_length=250, default='')
    image_of_person=models.ImageField(null=True,blank=True, upload_to=directory_path_to_reestr_personal_RUK_img)
    def __str__(self):
        return f'{self.fio}'

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Реестр Руководство'
    

