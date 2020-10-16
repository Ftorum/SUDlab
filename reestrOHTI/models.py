from django.db import models
from django.urls import reverse
from reestr_people.models import OHTI_reestr

# Create your models here.


# Средства измерения
def directory_path_to_OHTI_img(name_of_equipment, invent_number): 
    return 'images/OHTI/SI/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_verification(name_of_equipment, invent_number): 
    return 'images/OHTI/SI/varification/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_description_type(name_of_equipment, invent_number): 
    return 'images/OHTI/SI/description_type/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_method_file_poverka(name_of_equipment, invent_number): 
    return 'images/OHTI/SI/method_file_poverka/{0}/{1}'.format(name_of_equipment,invent_number)

class Equipment_SI_OHTI(models.Model):
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
    responsible_for_use = models.ForeignKey(OHTI_reestr,on_delete=models.SET_NULL,null=True)
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OHTI_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_OHTI_verification,null=True,blank=True)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_OHTI_description_type,null=True,blank=True)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_OHTI_method_file_poverka,null=True,blank=True)


    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    def get_absolute_url(self):
        return reverse ('ohti_SI_DATAIL', args=[str(self.id)])

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Средства измерения ОХТИ'
# Create your models here.





# Испытательное оборудование
def directory_path_to_OHTI_io_img(name_of_equipment, invent_number): 
    return 'images/OHTI/IO/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_io_verification(name_of_equipment, invent_number): 
    return 'images/OHTI/IO/varification/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_io_description_type(name_of_equipment, invent_number): 
    return 'images/OHTI/IO/description_type/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_io_method_file_poverka(name_of_equipment, invent_number): 
    return 'images/OHTI/IO/method_file_poverka/{0}/{1}'.format(name_of_equipment,invent_number)

class Equipment_IO_OHTI(models.Model):
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
    responsible_for_use = models.ForeignKey(OHTI_reestr,on_delete=models.SET_NULL,null=True)
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OHTI_io_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_OHTI_io_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_OHTI_io_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_OHTI_io_method_file_poverka,null=True,blank=True,)

    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    def get_absolute_url(self):
        return reverse ('ohti_IO_DATAIL', args=[str(self.id)])

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Испытательное оборудование ОХТИ'



# Вспомагательное оборудование
def directory_path_to_OHTI_vo_img(name_of_equipment, invent_number): 
    return 'images/OHTI/IO/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_vo_verification(name_of_equipment, invent_number): 
    return 'images/OHTI/IO/varification/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_vo_description_type(name_of_equipment, invent_number): 
    return 'images/OHTI/IO/description_type/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_vo_method_file_poverka(name_of_equipment, invent_number): 
    return 'images/OHTI/IO/method_file_poverka/{0}/{1}'.format(name_of_equipment,invent_number)

class Equipment_VO_OHTI(models.Model):
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
    responsible_for_use = models.ForeignKey(OHTI_reestr,on_delete=models.SET_NULL,null=True)
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OHTI_vo_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_OHTI_vo_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_OHTI_vo_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_OHTI_vo_method_file_poverka,null=True,blank=True,)



    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    def get_absolute_url(self):
        return reverse ('ohti_VO_DATAIL', args=[str(self.id)])

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Вспомогательное оборудование ОХТИ'


# Стеклянная мера 
def directory_path_to_OHTI_sm_img(name_of_equipment, invent_number): 
    return 'images/OHTI/SM/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equipment_SM_OHTI(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=150, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OHTI_sm_img)
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
    responsible_for_use = models.ForeignKey(OHTI_reestr,on_delete=models.SET_NULL,null=True,blank=True)
    fact = models.CharField('Примечание:', max_length=250, default='')


    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Стеклянная мера ОХТИ'


#Оборудование для отбора проб
def directory_path_to_OHTI_op_img(name_of_equipment, invent_number): 
    return 'images/OHTI/OP/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equipment_OP_OHTI(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=150, default='')
    name_as_passport = models.CharField('Наименование по паспорту:', max_length=150, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OHTI_op_img)
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
    responsible_for_use = models.ForeignKey(OHTI_reestr,on_delete=models.SET_NULL,null=True)
    fact = models.CharField('Примечание:', max_length=250, default='')

    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование для отбора проб ОХТИ'



#Вне области аккредитации
def directory_path_to_OHTI_voa_img(name_of_equipment, invent_number): 
    return 'images/OHTI/VOA/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_voa_verification(name_of_equipment, invent_number): 
    return 'images/OHTI/VOA/varification/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_voa_description_type(name_of_equipment, invent_number): 
    return 'images/OHTI/VOA/description_type/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_voa_method_file_poverka(name_of_equipment, invent_number): 
    return 'images/OHTI/VOA/method_file_poverka/{0}/{1}'.format(name_of_equipment,invent_number)
class Equipment_VOA_OHTI(models.Model):
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
    responsible_for_use = models.ForeignKey(OHTI_reestr,on_delete=models.SET_NULL,null=True)
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OHTI_voa_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_OHTI_voa_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_OHTI_voa_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_OHTI_voa_method_file_poverka,null=True,blank=True,)


    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    def get_absolute_url(self):
        return reverse ('ohti_VOA_DATAIL', args=[str(self.id)])

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Вне области аккредитации ОХТИ'



#Выведено из эксплуатации
def directory_path_to_OHTI_vu_img(name_of_equipment, invent_number): 
    return 'images/OHTI/VU/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_vu_proof_file(name_of_equipment, invent_number): 
    return 'images/OHTI/VU/proof_file/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equipment_VU_OHTI(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OHTI_vu_img)
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
    proof_file=models.FileField('Файл',upload_to=directory_path_to_OHTI_vu_proof_file,null=True,blank=True,)

    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Выведено из эксплуатации ОХТИ'


#Списаное лабораторное оборудование
def directory_path_to_OHTI_spi_img(name_of_equipment, invent_number): 
    return 'images/OHTI/SPI/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_spi_proof_file(name_of_equipment, invent_number): 
    return 'images/OHTI/SPI/proof_file/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equipment_SPI_OHTI(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OHTI_spi_img)
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
    proof_file=models.FileField('Файл',upload_to=directory_path_to_OHTI_spi_proof_file,null=True,blank=True,)

    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Списанное ЛО ОХТИ'


# _________________________________________________________________________________________
# модели запчастей, расходных материалов 
def directory_path_to_c_si_ohti_parts_img(name_of_equipment, invent_number): 
    return 'images/OHTI/SI/parts/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_si_ohti_parts_document(name_of_equipment, invent_number): 
    return 'images/OHTI/SI/parts/document/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equip_SI_part_OHTI(models.Model):
    name_of_equip=models.ForeignKey(Equipment_SI_OHTI, on_delete=models.SET_NULL,null=True,related_name='parts')
    name_of_part = models.CharField('Наименование запчасти(расходного материала):', max_length=150, default='')
    fact_number=models.CharField('Заводской номер (расходного материала):', max_length=150, default='')
    part_image = models.ImageField(null=True,blank=True, upload_to=directory_path_to_c_si_ohti_parts_img)
    part_docum=models.FileField('Файл',upload_to=directory_path_to_OHTI_si_ohti_parts_document,null=True,blank=True,)
    def __str__(self):
        return f'{self.name_of_equip}: {self.name_of_part}'

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти к Средствам измерения ОХТИ'


def directory_path_to_OHTI_io_parts_img(name_of_equipment, invent_number): 
    return 'images/OHTI/IO/parts/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_io_parts_document(name_of_equipment, invent_number): 
    return 'images/OHTI/IO/parts/document/{0}/{1}'.format(name_of_equipment,invent_number)
class Equip_IO_part_OHTI(models.Model):
    name_of_equip=models.ForeignKey(Equipment_IO_OHTI, on_delete=models.SET_NULL,null=True,related_name='parts')
    name_of_part = models.CharField('Наименование запчасти(расходного материала):', max_length=150, default='')
    fact_number=models.CharField('Заводской номер (расходного материала):', max_length=150, default='')
    part_image = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OHTI_io_parts_img)
    part_docum=models.FileField('Файл',upload_to=directory_path_to_OHTI_io_parts_document,null=True,blank=True,)
    def __str__(self):
        return f'{self.name_of_equip}: {self.name_of_part}'

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти к Испытательному оборудованию ОХТИ'


def directory_path_to_OHTI_vo_parts_img(name_of_equipment, invent_number): 
    return 'images/OHTI/VO/parts/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_vo_parts_document(name_of_equipment, invent_number): 
    return 'images/OHTI/VO/parts/document/{0}/{1}'.format(name_of_equipment,invent_number)
class Equip_VO_part_OHTI(models.Model):
    name_of_equip=models.ForeignKey(Equipment_VO_OHTI, on_delete=models.SET_NULL,null=True,related_name='parts')
    name_of_part = models.CharField('Наименование запчасти(расходного материала):', max_length=150, default='')
    fact_number=models.CharField('Заводской номер (расходного материала):', max_length=150, default='')
    part_image = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OHTI_vo_parts_img)
    part_docum=models.FileField('Файл',upload_to=directory_path_to_OHTI_vo_parts_document,null=True,blank=True,)
    def __str__(self):
        return f'{self.name_of_equip}: {self.name_of_part}'

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти к Вспомогательному оборудованию ОХТИ'


def directory_path_to_OHTI_voa_parts_img(name_of_equipment, invent_number): 
    return 'images/OHTI/VOA/parts/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OHTI_voa_parts_document(name_of_equipment, invent_number): 
    return 'images/OHTI/VOA/parts/document/{0}/{1}'.format(name_of_equipment,invent_number)        
class Equip_VOA_part_OHTI(models.Model):
    name_of_equip=models.ForeignKey(Equipment_VOA_OHTI, on_delete=models.SET_NULL,null=True,related_name='parts')
    name_of_part = models.CharField('Наименование запчасти(расходного материала):', max_length=150, default='')
    fact_number=models.CharField('Заводской номер (расходного материала):', max_length=150, default='')
    part_image = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OHTI_voa_parts_img)
    part_docum=models.FileField('Файл',upload_to=directory_path_to_OHTI_voa_parts_document,null=True,blank=True,)
    def __str__(self):
        return f'{self.name_of_equip}: {self.name_of_part}'

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти к Оборудованию вне области аккредитации ОХТИ'