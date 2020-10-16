from django.db import models
from django.urls import reverse
from reestr_people.models import OMVOiG_reestr

# Create your models here.


# Средства измерения
def directory_path_to_OMVOIG_img(name_of_equipment, invent_number): 
    return 'images/OMVOIG/SI/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_verification(name_of_equipment, invent_number): 
    return 'images/OMVOIG/SI/varification/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_description_type(name_of_equipment, invent_number): 
    return 'images/OMVOIG/SI/description_type/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_method_file_poverka(name_of_equipment, invent_number): 
    return 'images/OMVOIG/SI/method_file_poverka/{0}/{1}'.format(name_of_equipment,invent_number)

class Equipment_SI(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=250, default='')
    model_type = models.CharField('Модель, тип:', max_length=250, default='')
    number_gosreestr = models.CharField('Номер в госреестре СИ:', max_length=250, default='')
    po = models.CharField('Программное обеспечение', max_length=250, default='')
    company = models.CharField('Наименование компании производителя', max_length=250, default='')
    factury_number = models.CharField('Заводской Номер:', max_length=250, default='')
    invent_number = models.IntegerField('Инвентарный номер:', null=True)
    main_document = models.CharField('Наименование, шифр эксплуатационного документа:', max_length=200, default='')
    date_manufactur = models.CharField('Дата изготовления:', max_length=250, default='')
    date_start_usage = models.CharField('Дата ввода в эксплуатацию:', max_length=250, default='')
    location_lab = models.CharField('Место нахождения (кабинет):', max_length=250, default='')
    microclimate = models.CharField('Условия эксплуатации:', max_length=250, default='')
    range_of_measure = models.CharField('Предел (диапазон) измерений:', max_length=250, default='')
    class_measure = models.CharField('Класс точности, погрешность:', max_length=250, default='')
    organization_check = models.CharField('Организация, выполнившая поверку СИ:', max_length=250, default='')
    range_check = models.CharField('Переодичность поверки(мес):', max_length=250, default='')
    last_verification = models.CharField('Поверка СИ:',max_length=50, default='')
    last_maintaince = models.CharField('Техническое обслужинание, ремонт:', max_length=250, default='')
    tech_condition = models.CharField('Техническое состояние:', max_length=250, default='')
    responsible_for_use = models.ForeignKey(OMVOiG_reestr,on_delete=models.SET_NULL,null=True)
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMVOIG_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_OMVOIG_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_OMVOIG_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_OMVOIG_method_file_poverka,null=True,blank=True,)


    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    def get_absolute_url(self):
        return reverse ('omvoig_SI_DATAIL', args=[str(self.id)])

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Средства измерения ОМВОиГ'





# Испытательное оборудование
def directory_path_to_OMVOIG_io_img(name_of_equipment, invent_number): 
    return 'images/OMVOIG/IO/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_io_verification(name_of_equipment, invent_number): 
    return 'images/OMVOIG/IO/varification/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_io_description_type(name_of_equipment, invent_number): 
    return 'images/OMVOIG/IO/description_type/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_io_method_file_poverka(name_of_equipment, invent_number): 
    return 'images/OMVOIG/IO/method_file_poverka/{0}/{1}'.format(name_of_equipment,invent_number)

class Equipment_IO(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=150, default='')
    model_type = models.CharField('Модель, тип:', max_length=250, default='')
    po = models.CharField('Программное обеспечение', max_length=150, default='')
    company = models.CharField('Наименование компании производителя', max_length=250, default='')
    factury_number = models.CharField('Заводской Номер:', max_length=150, default='')
    invent_number = models.IntegerField('Инвентарный номер:', null=True)
    main_document = models.CharField('Наименование, шифр эксплуатационного документа:', max_length=200, default='')
    date_manufactur = models.CharField('Дата изготовления:', max_length=150, default='')
    date_get = models.CharField('Дата получения:', max_length=150, default='')
    date_start_usage = models.CharField('Дата ввода в эксплуатацию:', max_length=150, default='')
    location_lab = models.CharField('Место нахождения (кабинет):', max_length=150, default='')
    microclimate = models.CharField('Условия эксплуатации:', max_length=150, default='')
    organization_check = models.CharField('Организация, выполнившая аттестацию ИО:', max_length=150, default='')
    range_check = models.CharField('Переодичность аттестации(мес):', max_length=150, default='')
    last_verification = models.CharField('Аттестация ИО:',max_length=50, default='')
    last_maintaince = models.CharField('Техническое обслужинание, ремонт:', max_length=150, default='')
    tech_condition = models.CharField('Техническое состояние:', max_length=250, default='')
    responsible_for_use = models.ForeignKey(OMVOiG_reestr,on_delete=models.SET_NULL,null=True)
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMVOIG_io_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_OMVOIG_io_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_OMVOIG_io_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_OMVOIG_io_method_file_poverka,null=True,blank=True,)

    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    def get_absolute_url(self):
        return reverse ('omvoig_IO_DATAIL', args=[str(self.id)])

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Испытательное оборудование ОМВОиГ'


# Вспомагательное оборудование
def directory_path_to_OMVOIG_vo_img(name_of_equipment, invent_number): 
    return 'images/OMVOIG/IO/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_vo_verification(name_of_equipment, invent_number): 
    return 'images/OMVOIG/IO/varification/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_vo_description_type(name_of_equipment, invent_number): 
    return 'images/OMVOIG/IO/description_type/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_vo_method_file_poverka(name_of_equipment, invent_number): 
    return 'images/OMVOIG/IO/method_file_poverka/{0}/{1}'.format(name_of_equipment,invent_number)

class Equipment_VO(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=150, default='')
    model_type = models.CharField('Модель, тип:', max_length=250, default='')
    po = models.CharField('Программное обеспечение', max_length=150, default='')
    company = models.CharField('Наименование компании производителя', max_length=250, default='')
    factury_number = models.CharField('Заводской Номер:', max_length=150, default='')
    invent_number = models.IntegerField('Инвентарный номер:', null=True)
    pasport_cto = models.CharField('Паспорт по 174-2011 (дата утверждения):', max_length=200, default='')
    main_document = models.CharField('Наименование, шифр эксплуатационного документа:', max_length=200, default='')
    date_manufactur = models.CharField('Дата изготовления:', max_length=150, default='')
    date_start_usage = models.CharField('Дата ввода в эксплуатацию:', max_length=150, default='')
    location_lab = models.CharField('Место нахождения (кабинет):', max_length=150, default='')
    microclimate = models.CharField('Условия эксплуатации:', max_length=150, default='')
    last_maintaince = models.CharField('Техническое обслужинание, ремонт:', max_length=150, default='')
    tech_condition = models.CharField('Техническое состояние:', max_length=250, default='')
    responsible_for_use = models.ForeignKey(OMVOiG_reestr,on_delete=models.SET_NULL,null=True)
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMVOIG_vo_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_OMVOIG_vo_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_OMVOIG_vo_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_OMVOIG_vo_method_file_poverka,null=True,blank=True,)



    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    def get_absolute_url(self):
        return reverse ('omvoig_VO_DATAIL', args=[str(self.id)])

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Вспомогательное оборудование ОМВОиГ'




# Стеклянная мера 
def directory_path_to_OMVOIG_sm_img(name_of_equipment, invent_number): 
    return 'images/OMVOIG/SM/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equipment_SM(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=150, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMVOIG_sm_img)
    model_type = models.CharField('Модель, тип:', max_length=250, default='')
    number_gosreestr = models.CharField('Номер в госреестре СИ:', max_length=250, default='')
    po = models.CharField('Программное обеспечение', max_length=150, default='')
    company = models.CharField('Наименование компании производителя', max_length=250, default='')
    factury_number = models.CharField('Заводской Номер:', max_length=150, default='')
    invent_number = models.IntegerField('Инвентарный номер:', null=True)
    main_document = models.CharField('Наименование, шифр эксплуатационного документа:', max_length=200, default='')
    date_manufactur = models.CharField('Дата изготовления:', max_length=150, default='')
    date_start_usage = models.CharField('Дата ввода в эксплуатацию:', max_length=150, default='')
    location_lab = models.CharField('Место нахождения (кабинет):', max_length=150, default='')
    microclimate = models.CharField('Условия эксплуатации:', max_length=150, default='')
    range_of_measure = models.CharField('Предел (диапазон) измерений:', max_length=250, default='')
    class_measure = models.CharField('Класс точности, погрешность:', max_length=250, default='')
    organization_check = models.CharField('Организация, выполнившая поверку СИ:', max_length=250, default='')
    range_check = models.CharField('Переодичность поверки(мес):', max_length=250, default='')
    last_verification = models.CharField('Поверка СИ:',max_length=50, default='')
    last_maintaince = models.CharField('Техническое обслужинание, ремонт:', max_length=150, default='')
    tech_condition = models.CharField('Техническое состояние:', max_length=250, default='')
    responsible_for_use = models.ForeignKey(OMVOiG_reestr,on_delete=models.SET_NULL,null=True,blank=True)
    fact = models.CharField('Примечание:', max_length=250, default='')


    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Стеклянная мера ОМВОиГ'


#Оборудование для отбора проб
def directory_path_to_OMVOIG_op_img(name_of_equipment, invent_number): 
    return 'images/OMVOIG/OP/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equipment_OP(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=150, default='')
    name_as_passport = models.CharField('Наименование по паспорту:', max_length=150, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMVOIG_op_img)
    model_type = models.CharField('Модель, тип:', max_length=250, default='')
    number_gosreestr = models.CharField('Номер в госреестре СИ:', max_length=250, default='')
    po = models.CharField('Программное обеспечение', max_length=150, default='')
    company = models.CharField('Наименование компании производителя', max_length=250, default='')
    pasport_cto = models.CharField('Паспорт по 174-2011 (дата утверждения):', max_length=200, default='')
    factury_number = models.CharField('Заводской Номер:', max_length=150, default='')
    invent_number = models.IntegerField('Инвентарный номер:', null=True)
    main_document = models.CharField('Наименование, шифр эксплуатационного документа:', max_length=200, default='')
    date_get = models.CharField('Дата получения:', max_length=150, default='')
    date_start_usage = models.CharField('Дата ввода в эксплуатацию:', max_length=150, default='')
    location_lab = models.CharField('Место нахождения (кабинет):', max_length=150, default='')
    microclimate = models.CharField('Условия эксплуатации:', max_length=150, default='')
    responsible_for_use = models.ForeignKey(OMVOiG_reestr,on_delete=models.SET_NULL,null=True)
    fact = models.CharField('Примечание:', max_length=250, default='')

    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование для отбора проб ОМВОиГ'


#Вне области аккредитации
def directory_path_to_OMVOIG_voa_img(name_of_equipment, invent_number): 
    return 'images/OMVOIG/VOA/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_voa_verification(name_of_equipment, invent_number): 
    return 'images/OMVOIG/VOA/varification/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_voa_description_type(name_of_equipment, invent_number): 
    return 'images/OMVOIG/VOA/description_type/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_voa_method_file_poverka(name_of_equipment, invent_number): 
    return 'images/OMVOIG/VOA/method_file_poverka/{0}/{1}'.format(name_of_equipment,invent_number)
class Equipment_VOA(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=250, default='')
    model_type = models.CharField('Модель, тип:', max_length=250, default='')
    number_gosreestr = models.CharField('Номер в госреестре СИ:', max_length=250, default='')
    po = models.CharField('Программное обеспечение', max_length=250, default='')
    company = models.CharField('Наименование компании производителя', max_length=250, default='')
    factury_number = models.CharField('Заводской Номер:', max_length=250, default='')
    invent_number = models.IntegerField('Инвентарный номер:', null=True)
    main_document = models.CharField('Наименование, шифр эксплуатационного документа:', max_length=200, default='')
    date_manufactur = models.CharField('Дата изготовления:', max_length=250, default='')
    date_start_usage = models.CharField('Дата ввода в эксплуатацию:', max_length=250, default='')
    location_lab = models.CharField('Место нахождения (кабинет):', max_length=250, default='')
    microclimate = models.CharField('Условия эксплуатации:', max_length=250, default='')
    range_of_measure = models.CharField('Предел (диапазон) измерений:', max_length=250, default='')
    class_measure = models.CharField('Класс точности, погрешность:', max_length=250, default='')
    organization_check = models.CharField('Организация, выполнившая поверку, калибровку СИ:', max_length=250, default='')
    range_check = models.CharField('Переодичность поверки, калибровки(мес):', max_length=250, default='')
    last_verification = models.CharField('Поверка, аттестация СИ:',max_length=50, default='')
    last_maintaince = models.CharField('Техническое обслужинание, ремонт:', max_length=250, default='')
    tech_condition = models.CharField('Техническое состояние:', max_length=250, default='')
    responsible_for_use = models.ForeignKey(OMVOiG_reestr,on_delete=models.SET_NULL,null=True)
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMVOIG_voa_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_OMVOIG_voa_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_OMVOIG_voa_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_OMVOIG_voa_method_file_poverka,null=True,blank=True,)


    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    def get_absolute_url(self):
        return reverse ('omvoig_VOA_DATAIL', args=[str(self.id)])

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Вне области аккредитации ОМВОиГ'


#Выведено из эксплуатации
def directory_path_to_OMVOIG_vu_img(name_of_equipment, invent_number): 
    return 'images/OMVOIG/VU/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_vu_proof_file(name_of_equipment, invent_number): 
    return 'images/OMVOIG/VU/proof_file/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equipment_VU(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMVOIG_voa_img)
    model_type = models.CharField('Модель, тип:', max_length=250, default='')
    company = models.CharField('Наименование компании производителя', max_length=250, default='')
    factury_number = models.CharField('Заводской Номер:', max_length=250, default='')
    invent_number = models.IntegerField('Инвентарный номер:', null=True)
    date_manufactur = models.CharField('Дата изготовления:', max_length=250, default='')
    date_start_usage = models.CharField('Дата ввода в эксплуатацию:', max_length=250, default='')
    location_lab = models.CharField('Место нахождения (кабинет):', max_length=250, default='')
    date_end_usage = models.CharField('Дата вывода из эксплуатации:', max_length=250, default='')
    reason_of_out = models.CharField('Причина вывода из эксплуатации:', max_length=250, default='')
    fact = models.CharField('Примечание:', max_length=250, default='')
    proof_file=models.FileField('Файл',upload_to=directory_path_to_OMVOIG_vu_proof_file,null=True,blank=True,)

    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Выведено из эксплуатации ОМВОиГ'



#Списаное лабораторное оборудование
def directory_path_to_OMVOIG_spi_img(name_of_equipment, invent_number): 
    return 'images/OMVOIG/SPI/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_spi_proof_file(name_of_equipment, invent_number): 
    return 'images/OMVOIG/SPI/proof_file/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equipment_SPI(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMVOIG_spi_img)
    model_type = models.CharField('Модель, тип:', max_length=250, default='')
    company = models.CharField('Наименование компании производителя', max_length=250, default='')
    factury_number = models.CharField('Заводской Номер:', max_length=250, default='')
    invent_number = models.IntegerField('Инвентарный номер:', null=True)
    date_manufactur = models.CharField('Дата изготовления:', max_length=250, default='')
    date_start_usage = models.CharField('Дата ввода в эксплуатацию:', max_length=250, default='')
    location_lab = models.CharField('Место нахождения (кабинет):', max_length=250, default='')
    date_end_usage = models.CharField('Дата вывода из эксплуатации:', max_length=250, default='')
    reason_of_out = models.CharField('Причина вывода из эксплуатации:', max_length=250, default='')
    fact = models.CharField('Примечание:', max_length=250, default='')
    proof_file=models.FileField('Файл',upload_to=directory_path_to_OMVOIG_spi_proof_file,null=True,blank=True,)

    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Списанное ЛО ОМВОиГ'


# _________________________________________________________________________________________
# модели запчастей, расходных материалов 
def directory_path_to_OMVOIG_si_parts_img(name_of_equipment, invent_number): 
    return 'images/OMVOIG/SI/parts/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_si_parts_document(name_of_equipment, invent_number): 
    return 'images/OMVOIG/SI/parts/document/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equip_SI_part(models.Model):
    name_of_equip=models.ForeignKey(Equipment_SI, on_delete=models.SET_NULL,null=True,related_name='parts')
    name_of_part = models.CharField('Наименование запчасти(расходного материала):', max_length=150, default='')
    fact_number=models.CharField('Заводской номер (расходного материала):', max_length=150, default='')
    part_image = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMVOIG_si_parts_img)
    part_docum=models.FileField('Файл',upload_to=directory_path_to_OMVOIG_si_parts_document,null=True,blank=True,)
    def __str__(self):
        return f'{self.name_of_equip}: {self.name_of_part}'

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти к Средствам измерения ОМВОиГ'


def directory_path_to_OMVOIG_io_parts_img(name_of_equipment, invent_number): 
    return 'images/OMVOIG/IO/parts/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_io_parts_document(name_of_equipment, invent_number): 
    return 'images/OMVOIG/IO/parts/document/{0}/{1}'.format(name_of_equipment,invent_number)
class Equip_IO_part(models.Model):
    name_of_equip=models.ForeignKey(Equipment_IO, on_delete=models.SET_NULL,null=True,related_name='parts')
    name_of_part = models.CharField('Наименование запчасти(расходного материала):', max_length=150, default='')
    fact_number=models.CharField('Заводской номер (расходного материала):', max_length=150, default='')
    part_image = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMVOIG_io_parts_img)
    part_docum=models.FileField('Файл',upload_to=directory_path_to_OMVOIG_io_parts_document,null=True,blank=True,)
    def __str__(self):
        return f'{self.name_of_equip}: {self.name_of_part}'

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти к Испытательному оборудованию ОМВОиГ'




def directory_path_to_OMVOIG_vo_parts_img(name_of_equipment, invent_number): 
    return 'images/OMVOIG/VO/parts/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_vo_parts_document(name_of_equipment, invent_number): 
    return 'images/OMVOIG/VO/parts/document/{0}/{1}'.format(name_of_equipment,invent_number)
class Equip_VO_part(models.Model):
    name_of_equip=models.ForeignKey(Equipment_VO, on_delete=models.SET_NULL,null=True,related_name='parts')
    name_of_part = models.CharField('Наименование запчасти(расходного материала):', max_length=150, default='')
    fact_number=models.CharField('Заводской номер (расходного материала):', max_length=150, default='')
    part_image = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMVOIG_vo_parts_img)
    part_docum=models.FileField('Файл',upload_to=directory_path_to_OMVOIG_vo_parts_document,null=True,blank=True,)
    def __str__(self):
        return f'{self.name_of_equip}: {self.name_of_part}'

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти к Вспомогательному оборудованию ОМВОиГ'



def directory_path_to_OMVOIG_voa_parts_img(name_of_equipment, invent_number): 
    return 'images/OMVOIG/VOA/parts/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMVOIG_voa_parts_document(name_of_equipment, invent_number): 
    return 'images/OMVOIG/VOA/parts/document/{0}/{1}'.format(name_of_equipment,invent_number)        
class Equip_VOA_part(models.Model):
    name_of_equip=models.ForeignKey(Equipment_VOA, on_delete=models.SET_NULL,null=True,related_name='parts')
    name_of_part = models.CharField('Наименование запчасти(расходного материала):', max_length=150, default='')
    fact_number=models.CharField('Заводской номер (расходного материала):', max_length=150, default='')
    part_image = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMVOIG_voa_parts_img)
    part_docum=models.FileField('Файл',upload_to=directory_path_to_OMVOIG_voa_parts_document,null=True,blank=True,)
    def __str__(self):
        return f'{self.name_of_equip}: {self.name_of_part}'

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти к Оборудованию вне области аккредитации ОМВОиГ'








