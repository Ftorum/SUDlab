from django.db import models
from django.urls import reverse
from reestr_people.models import ORIMP_reestr
# Create your models here.

# Средства измерения
def directory_path_to_ORIMP_img(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/SI/{0}/{1}'.format(name_of_equipment_passport,invent_number) 
def directory_path_to_ORIMP_verification(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/SI/varification/{0}/{1}'.format(name_of_equipment_passport,invent_number) 
def directory_path_to_ORIMP_description_type(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/SI/description_type/{0}/{1}'.format(name_of_equipment_passport,invent_number) 
def directory_path_to_ORIMP_method_file_poverka(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/SI/method_file_poverka/{0}/{1}'.format(name_of_equipment_passport,invent_number)

class Equipment_SI_ORIMP(models.Model):
    name_of_equipment_passport = models.CharField('Наименование оборудования по паспорту:', max_length=250, default='')
    name_of_equipment_gos_reestr = models.CharField('Наименование оборудования по госреестру:', max_length=250, default='')
    equip_R3 = models.CharField('Наименование оборудования R3:', max_length=250, default='')
    model_type = models.CharField('Модель, тип:', max_length=250, default='')
    number_gosreestr = models.CharField('Номер в госреестре СИ:', max_length=250, default='')
    number_etalon = models.CharField('Регистрационный номер эталона:', max_length=250, default='')
    po = models.CharField('Программное обеспечение', max_length=250, default='')
    company = models.CharField('Наименование компании производителя', max_length=250, default='')
    factury_number = models.CharField('Заводской Номер:', max_length=250, default='')
    invent_number = models.IntegerField('Инвентарный номер:', null=True)
    main_document = models.CharField('Наименование, шифр эксплуатационного документа:', max_length=200, default='')
    range_of_measure = models.CharField('Предел (диапазон) измерений:', max_length=250, default='')
    class_measure = models.CharField('Класс точности, погрешность:', max_length=250, default='')
    location_lab = models.CharField('Место нахождения (кабинет):', max_length=250, default='')
    microclimate = models.CharField('Условия эксплуатации:', max_length=250, default='')
    organization_check = models.CharField('Организация, выполнившая поверку СИ:', max_length=250, default='')
    range_check = models.CharField('Переодичность поверки(мес):', max_length=250, default='')
    last_verification = models.CharField('Поверка СИ:',max_length=50, default='')
    next_verification = models.CharField('Дата следующей поверки/калибровки/аттестации:',max_length=50, default='')
    last_maintaince = models.CharField('Техническое обслужинание, ремонт:', max_length=250, default='')
    tech_condition = models.CharField('Техническое состояние:', max_length=250, default='')
    responsible_for_use = models.ForeignKey(ORIMP_reestr,on_delete=models.SET_NULL,null=True)
    date_manufactur = models.CharField('Дата изготовления:', max_length=250, default='')
    date_start_usage = models.CharField('Дата ввода в эксплуатацию:', max_length=250, default='')
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_ORIMP_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_ORIMP_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_ORIMP_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_ORIMP_method_file_poverka,null=True,blank=True,)


    def __str__(self):
        return f'{self.name_of_equipment_passport}: {self.model_type}'

    def get_absolute_url(self):
        return reverse ('orimp_SI_DATAIL', args=[str(self.id)])

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Средства измерения ОРиМР'



# Испытательное оборудование
def directory_path_to_ORIMP_io_img(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/IO/{0}/{1}'.format(name_of_equipment_passport,invent_number) 
def directory_path_to_ORIMP_io_verification(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/IO/varification/{0}/{1}'.format(name_of_equipment_passport,invent_number) 
def directory_path_to_ORIMP_io_description_type(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/IO/description_type/{0}/{1}'.format(name_of_equipment_passport,invent_number) 
def directory_path_to_ORIMP_io_method_file_poverka(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/IO/method_file_poverka/{0}/{1}'.format(name_of_equipment_passport,invent_number)

class Equipment_IO_ORIMP(models.Model):
    name_of_equipment_passport = models.CharField('Наименование оборудования по паспорту:', max_length=250, default='')
    name_of_equipment_gos_reestr = models.CharField('Наименование оборудования по госреестру:', max_length=250, default='')
    equip_R3 = models.CharField('Наименование оборудования R3:', max_length=250, default='')
    model_type = models.CharField('Модель, тип:', max_length=250, default='')
    number_gosreestr = models.CharField('Номер в госреестре СИ:', max_length=250, default='')
    number_etalon = models.CharField('Регистрационный номер эталона:', max_length=250, default='')
    po = models.CharField('Программное обеспечение', max_length=250, default='')
    company = models.CharField('Наименование компании производителя', max_length=250, default='')
    factury_number = models.CharField('Заводской Номер:', max_length=250, default='')
    invent_number = models.IntegerField('Инвентарный номер:', null=True)
    main_document = models.CharField('Наименование, шифр эксплуатационного документа:', max_length=200, default='')
    range_of_measure = models.CharField('Предел (диапазон) измерений:', max_length=250, default='')
    class_measure = models.CharField('Класс точности, погрешность:', max_length=250, default='')
    location_lab = models.CharField('Место нахождения (кабинет):', max_length=250, default='')
    microclimate = models.CharField('Условия эксплуатации:', max_length=250, default='')
    organization_check = models.CharField('Организация, выполнившая поверку СИ:', max_length=250, default='')
    range_check = models.CharField('Переодичность поверки(мес):', max_length=250, default='')
    last_verification = models.CharField('Поверка СИ:',max_length=50, default='')
    next_verification = models.CharField('Дата следующей поверки/калибровки/аттестации:',max_length=50, default='')
    last_maintaince = models.CharField('Техническое обслужинание, ремонт:', max_length=250, default='')
    tech_condition = models.CharField('Техническое состояние:', max_length=250, default='')
    responsible_for_use = models.ForeignKey(ORIMP_reestr,on_delete=models.SET_NULL,null=True)
    date_manufactur = models.CharField('Дата изготовления:', max_length=250, default='')
    date_start_usage = models.CharField('Дата ввода в эксплуатацию:', max_length=250, default='')
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_ORIMP_io_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_ORIMP_io_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_ORIMP_io_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_ORIMP_io_method_file_poverka,null=True,blank=True,)


    def __str__(self):
        return f'{self.name_of_equipment_passport}: {self.model_type}'

    def get_absolute_url(self):
        return reverse ('orimp_IO_DATAIL', args=[str(self.id)])

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Испытательное оборудование ОРиМР'


# Вспомогательное оборудование
def directory_path_to_ORIMP_vo_img(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/VO/{0}/{1}'.format(name_of_equipment_passport,invent_number) 
def directory_path_to_ORIMP_vo_verification(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/VO/varification/{0}/{1}'.format(name_of_equipment_passport,invent_number) 
def directory_path_to_ORIMP_vo_description_type(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/VO/description_type/{0}/{1}'.format(name_of_equipment_passport,invent_number) 
def directory_path_to_ORIMP_vo_method_file_poverka(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/VO/method_file_poverka/{0}/{1}'.format(name_of_equipment_passport,invent_number)

class Equipment_VO_ORIMP(models.Model):
    name_of_equipment_passport = models.CharField('Наименование оборудования по паспорту:', max_length=250, default='')
    name_of_equipment_gos_reestr = models.CharField('Наименование оборудования по госреестру:', max_length=250, default='')
    equip_R3 = models.CharField('Наименование оборудования R3:', max_length=250, default='')
    model_type = models.CharField('Модель, тип:', max_length=250, default='')
    number_gosreestr = models.CharField('Номер в госреестре СИ:', max_length=250, default='')
    number_etalon = models.CharField('Регистрационный номер эталона:', max_length=250, default='')
    po = models.CharField('Программное обеспечение', max_length=250, default='')
    company = models.CharField('Наименование компании производителя', max_length=250, default='')
    factury_number = models.CharField('Заводской Номер:', max_length=250, default='')
    invent_number = models.IntegerField('Инвентарный номер:', null=True)
    main_document = models.CharField('Наименование, шифр эксплуатационного документа:', max_length=200, default='')
    range_of_measure = models.CharField('Предел (диапазон) измерений:', max_length=250, default='')
    class_measure = models.CharField('Класс точности, погрешность:', max_length=250, default='')
    location_lab = models.CharField('Место нахождения (кабинет):', max_length=250, default='')
    microclimate = models.CharField('Условия эксплуатации:', max_length=250, default='')
    organization_check = models.CharField('Организация, выполнившая поверку СИ:', max_length=250, default='')
    range_check = models.CharField('Переодичность поверки(мес):', max_length=250, default='')
    last_verification = models.CharField('Поверка СИ:',max_length=50, default='')
    next_verification = models.CharField('Дата следующей поверки/калибровки/аттестации:',max_length=50, default='')
    last_maintaince = models.CharField('Техническое обслужинание, ремонт:', max_length=250, default='')
    tech_condition = models.CharField('Техническое состояние:', max_length=250, default='')
    responsible_for_use = models.ForeignKey(ORIMP_reestr,on_delete=models.SET_NULL,null=True)
    date_manufactur = models.CharField('Дата изготовления:', max_length=250, default='')
    date_start_usage = models.CharField('Дата ввода в эксплуатацию:', max_length=250, default='')
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_ORIMP_vo_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_ORIMP_vo_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_ORIMP_vo_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_ORIMP_vo_method_file_poverka,null=True,blank=True,)


    def __str__(self):
        return f'{self.name_of_equipment_passport}: {self.model_type}'

    def get_absolute_url(self):
        return reverse ('orimp_VO_DATAIL', args=[str(self.id)])

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Вспомогательное оборудование ОРиМР'


# Перечень эталонов
def directory_path_to_ORIMP_et_img(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/ET/{0}/{1}'.format(name_of_equipment_passport,invent_number) 
def directory_path_to_ORIMP_et_verification(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/ET/varification/{0}/{1}'.format(name_of_equipment_passport,invent_number) 
def directory_path_to_ORIMP_et_description_type(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/ET/description_type/{0}/{1}'.format(name_of_equipment_passport,invent_number) 
def directory_path_to_ORIMP_et_method_file_poverka(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/ET/method_file_poverka/{0}/{1}'.format(name_of_equipment_passport,invent_number)

class Equipment_ET_ORIMP(models.Model):
    reg_number=models.CharField('Регистрационный номер эталона:', max_length=250, default='')
    name_of_equipment_passport = models.CharField('Наименование оборудования по паспорту:', max_length=250, default='')
    name_of_equipment_measure = models.CharField('Наименование средств измерений:', max_length=250, default='')
    factury_number = models.CharField('Заводской Номер:', max_length=250, default='')
    main_document = models.CharField('Приказ об утверждени эталонов единиц величин:', max_length=200, default='')
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_ORIMP_et_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_ORIMP_et_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_ORIMP_et_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_ORIMP_et_method_file_poverka,null=True,blank=True,)


    def __str__(self):
        return f'{self.name_of_equipment_passport}: {self.factury_number}'

    class Meta:
        verbose_name = 'Эталон'
        verbose_name_plural = 'Перечень эталонов ОРиМР'


# Перечень эталонов
def directory_path_to_ORIMP_ret_img(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/RET/{0}/{1}'.format(name_of_equipment_passport,invent_number) 
def directory_path_to_ORIMP_ret_verification(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/RET/varification/{0}/{1}'.format(name_of_equipment_passport,invent_number) 
def directory_path_to_ORIMP_ret_description_type(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/RET/description_type/{0}/{1}'.format(name_of_equipment_passport,invent_number) 
def directory_path_to_ORIMP_ret_method_file_poverka(name_of_equipment_passport, invent_number): 
    return 'images/ORIMP/RET/method_file_poverka/{0}/{1}'.format(name_of_equipment_passport,invent_number)

class Equipment_RET_ORIMP(models.Model):
    reg_number=models.CharField('Регистрационный номер эталона:', max_length=250, default='')
    name_of_equipment_passport = models.CharField('Наименование оборудования по паспорту:', max_length=250, default='')
    name_of_equipment_measure = models.CharField('Наименование средств измерений:', max_length=250, default='')
    factury_number = models.CharField('Заводской Номер:', max_length=250, default='')
    fact = models.CharField('Примечание:', max_length=250, default='')
    numb_elect_zayavki = models.CharField('Номер электронной заявки:', max_length=250, default='')
    date_next_verification = models.CharField('Дата следующей поверки:', max_length=250, default='')
    date_attestation_et = models.CharField('Дата аттестации элатона:', max_length=250, default='')
    scheme_of_verivication = models.TextField('Наименование Государственной поверочной схемы для средств измерений:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_ORIMP_ret_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_ORIMP_ret_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_ORIMP_ret_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_ORIMP_ret_method_file_poverka,null=True,blank=True,)

    def __str__(self):
        return f'{self.name_of_equipment_passport}: {self.factury_number}'

    class Meta:
        verbose_name = 'Эталон'
        verbose_name_plural = 'Реестр эталонов ОРиМР'



# _________________________________________________________________________________________
# модели запчастей, расходных материалов 
def directory_path_to_c_si_ORIMP_parts_img(name_of_equipment, invent_number): 
    return 'images/ORIMP/SI/parts/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_ORIMP_si_ohti_parts_document(name_of_equipment, invent_number): 
    return 'images/ORIMP/SI/parts/document/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equip_SI_part_ORIMP(models.Model):
    name_of_equip=models.ForeignKey(Equipment_SI_ORIMP, on_delete=models.SET_NULL,null=True,related_name='parts')
    name_of_part = models.CharField('Наименование запчасти(расходного материала):', max_length=150, default='')
    fact_number=models.CharField('Заводской номер (расходного материала):', max_length=150, default='')
    part_image = models.ImageField(null=True,blank=True, upload_to=directory_path_to_c_si_ORIMP_parts_img)
    part_docum=models.FileField('Файл',upload_to=directory_path_to_ORIMP_si_ohti_parts_document,null=True,blank=True,)
    def __str__(self):
        return f'{self.name_of_equip}: {self.name_of_part}'

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти к Средствам измерения ОРиМР'


def directory_path_to_ORIMP_io_parts_img(name_of_equipment, invent_number): 
    return 'images/ORIMP/IO/parts/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_ORIMP_io_parts_document(name_of_equipment, invent_number): 
    return 'images/ORIMP/IO/parts/document/{0}/{1}'.format(name_of_equipment,invent_number)
class Equip_IO_part_ORIMP(models.Model):
    name_of_equip=models.ForeignKey(Equipment_IO_ORIMP, on_delete=models.SET_NULL,null=True,related_name='parts')
    name_of_part = models.CharField('Наименование запчасти(расходного материала):', max_length=150, default='')
    fact_number=models.CharField('Заводской номер (расходного материала):', max_length=150, default='')
    part_image = models.ImageField(null=True,blank=True, upload_to=directory_path_to_ORIMP_io_parts_img)
    part_docum=models.FileField('Файл',upload_to=directory_path_to_ORIMP_io_parts_document,null=True,blank=True,)
    def __str__(self):
        return f'{self.name_of_equip}: {self.name_of_part}'

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти к Испытательному оборудованию ОРиМР'


def directory_path_to_ORIMP_vo_parts_img(name_of_equipment, invent_number): 
    return 'images/ORIMP/VO/parts/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_ORIMP_vo_parts_document(name_of_equipment, invent_number): 
    return 'images/ORIMP/VO/parts/document/{0}/{1}'.format(name_of_equipment,invent_number)
class Equip_VO_part_ORIMP(models.Model):
    name_of_equip=models.ForeignKey(Equipment_VO_ORIMP, on_delete=models.SET_NULL,null=True,related_name='parts')
    name_of_part = models.CharField('Наименование запчасти(расходного материала):', max_length=150, default='')
    fact_number=models.CharField('Заводской номер (расходного материала):', max_length=150, default='')
    part_image = models.ImageField(null=True,blank=True, upload_to=directory_path_to_ORIMP_vo_parts_img)
    part_docum=models.FileField('Файл',upload_to=directory_path_to_ORIMP_vo_parts_document,null=True,blank=True,)
    def __str__(self):
        return f'{self.name_of_equip}: {self.name_of_part}'

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти к Вспомогательному оборудованию ОРиМР'