from django.db import models
from django.urls import reverse
from reestr_people.models import OMFF_reestr

# Create your models here.
# Средства измерения
def directory_path_to_OMFF_img(name_of_equipment, invent_number): 
    return 'images/OMFF/SI/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_verification(name_of_equipment, invent_number): 
    return 'images/OMFF/SI/varification/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_description_type(name_of_equipment, invent_number): 
    return 'images/OMFF/SI/description_type/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_method_file_poverka(name_of_equipment, invent_number): 
    return 'images/OMFF/SI/method_file_poverka/{0}/{1}'.format(name_of_equipment,invent_number)

class Equipment_SI_OMFF(models.Model):
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
    responsible_for_use = models.ForeignKey(OMFF_reestr,on_delete=models.SET_NULL,null=True)
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMFF_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_OMFF_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_OMFF_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_OMFF_method_file_poverka,null=True,blank=True,)


    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    def get_absolute_url(self):
        return reverse ('omff_SI_DATAIL', args=[str(self.id)])

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Средства измерения ОМФФ'


# Испытательное оборудование
def directory_path_to_OMFF_io_img(name_of_equipment, invent_number): 
    return 'images/OMFF/IO/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_io_verification(name_of_equipment, invent_number): 
    return 'images/OMFF/IO/varification/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_io_description_type(name_of_equipment, invent_number): 
    return 'images/OMFF/IO/description_type/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_io_method_file_poverka(name_of_equipment, invent_number): 
    return 'images/OMFF/IO/method_file_poverka/{0}/{1}'.format(name_of_equipment,invent_number)

class Equipment_IO_OMFF(models.Model):
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
    responsible_for_use = models.ForeignKey(OMFF_reestr,on_delete=models.SET_NULL,null=True)
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMFF_io_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_OMFF_io_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_OMFF_io_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_OMFF_io_method_file_poverka,null=True,blank=True,)

    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    def get_absolute_url(self):
        return reverse ('omff_IO_DATAIL', args=[str(self.id)])

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Испытательное оборудование ОМФФ'


# Вспомагательное оборудование
def directory_path_to_OMFF_vo_img(name_of_equipment, invent_number): 
    return 'images/OMFF/IO/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_vo_verification(name_of_equipment, invent_number): 
    return 'images/OMFF/IO/varification/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_vo_description_type(name_of_equipment, invent_number): 
    return 'images/OMFF/IO/description_type/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_vo_method_file_poverka(name_of_equipment, invent_number): 
    return 'images/OMFF/IO/method_file_poverka/{0}/{1}'.format(name_of_equipment,invent_number)

class Equipment_VO_OMFF(models.Model):
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
    responsible_for_use = models.ForeignKey(OMFF_reestr,on_delete=models.SET_NULL,null=True)
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMFF_vo_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_OMFF_vo_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_OMFF_vo_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_OMFF_vo_method_file_poverka,null=True,blank=True,)



    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    def get_absolute_url(self):
        return reverse ('omff_VO_DATAIL', args=[str(self.id)])

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Вспомогательное оборудование ОМФФ'


# Стеклянная мера 
def directory_path_to_OMFF_sm_img(name_of_equipment, invent_number): 
    return 'images/OMFF/SM/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equipment_SM_OMFF(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=150, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMFF_sm_img)
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
    responsible_for_use = models.ForeignKey(OMFF_reestr,on_delete=models.SET_NULL,null=True,blank=True)
    fact = models.CharField('Примечание:', max_length=250, default='')


    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Стеклянная мера ОМФФ'


#Оборудование для отбора проб
def directory_path_to_OMFF_op_img(name_of_equipment, invent_number): 
    return 'images/v/OP/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equipment_OP_OMFF(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=150, default='')
    name_as_passport = models.CharField('Наименование по паспорту:', max_length=150, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMFF_op_img)
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
    responsible_for_use = models.ForeignKey(OMFF_reestr,on_delete=models.SET_NULL,null=True)
    fact = models.CharField('Примечание:', max_length=250, default='')

    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование для отбора проб ОМФФ'

#Вне области аккредитации
def directory_path_to_OMFF_voa_img(name_of_equipment, invent_number): 
    return 'images/OMFF/VOA/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_voa_verification(name_of_equipment, invent_number): 
    return 'images/OMFF/VOA/varification/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_voa_description_type(name_of_equipment, invent_number): 
    return 'images/OMFF/VOA/description_type/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_voa_method_file_poverka(name_of_equipment, invent_number): 
    return 'images/OMFF/VOA/method_file_poverka/{0}/{1}'.format(name_of_equipment,invent_number)
class Equipment_VOA_OMFF(models.Model):
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
    responsible_for_use = models.ForeignKey(OMFF_reestr,on_delete=models.SET_NULL,null=True)
    fact = models.CharField('Примечание:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMFF_voa_img)
    verification_file=models.FileField('Файл поверки',upload_to=directory_path_to_OMFF_voa_verification,null=True,blank=True,)
    description_type=models.FileField('Описание типа',upload_to=directory_path_to_OMFF_voa_description_type,null=True,blank=True,)
    method_file_poverka=models.FileField('Методика поверки/аттестации',upload_to=directory_path_to_OMFF_voa_method_file_poverka,null=True,blank=True,)


    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    def get_absolute_url(self):
        return reverse ('omff_VOA_DATAIL', args=[str(self.id)])

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Вне области аккредитации ОМФФ'


#Выведено из эксплуатации
def directory_path_to_OMFF_vu_img(name_of_equipment, invent_number): 
    return 'images/OMFF/VU/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_vu_proof_file(name_of_equipment, invent_number): 
    return 'images/OMFF/VU/proof_file/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equipment_VU_OMFF(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMFF_vu_img)
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
    proof_file=models.FileField('Файл',upload_to=directory_path_to_OMFF_vu_proof_file,null=True,blank=True,)

    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Выведено из эксплуатации ОМФФ'


#Списаное лабораторное оборудование
def directory_path_to_OMFF_spi_img(name_of_equipment, invent_number): 
    return 'images/OMFF/SPI/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_spi_proof_file(name_of_equipment, invent_number): 
    return 'images/OMFF/SPI/proof_file/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equipment_SPI_OMFF(models.Model):
    name_of_equipment = models.CharField('Наименование оборудования:', max_length=250, default='')
    image_of_equipment = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMFF_spi_img)
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
    proof_file=models.FileField('Файл',upload_to=directory_path_to_OMFF_spi_proof_file,null=True,blank=True,)

    def __str__(self):
        return f'{self.name_of_equipment}: {self.model_type}'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Списанное ЛО ОМФФ'



# _________________________________________________________________________________________
# модели запчастей, расходных материалов 
def directory_path_to_c_si_OMFF_parts_img(name_of_equipment, invent_number): 
    return 'images/OMFF/SI/parts/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_si_ohti_parts_document(name_of_equipment, invent_number): 
    return 'images/OMFF/SI/parts/document/{0}/{1}'.format(name_of_equipment,invent_number) 
class Equip_SI_part_OMFF(models.Model):
    name_of_equip=models.ForeignKey(Equipment_SI_OMFF, on_delete=models.SET_NULL,null=True,related_name='parts')
    name_of_part = models.CharField('Наименование запчасти(расходного материала):', max_length=150, default='')
    fact_number=models.CharField('Заводской номер (расходного материала):', max_length=150, default='')
    part_image = models.ImageField(null=True,blank=True, upload_to=directory_path_to_c_si_OMFF_parts_img)
    part_docum=models.FileField('Файл',upload_to=directory_path_to_OMFF_si_ohti_parts_document,null=True,blank=True,)
    def __str__(self):
        return f'{self.name_of_equip}: {self.name_of_part}'

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти к Средствам измерения ОМФФ'


def directory_path_to_OMFF_io_parts_img(name_of_equipment, invent_number): 
    return 'images/OMFF/IO/parts/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_io_parts_document(name_of_equipment, invent_number): 
    return 'images/OMFF/IO/parts/document/{0}/{1}'.format(name_of_equipment,invent_number)
class Equip_IO_part_OMFF(models.Model):
    name_of_equip=models.ForeignKey(Equipment_IO_OMFF, on_delete=models.SET_NULL,null=True,related_name='parts')
    name_of_part = models.CharField('Наименование запчасти(расходного материала):', max_length=150, default='')
    fact_number=models.CharField('Заводской номер (расходного материала):', max_length=150, default='')
    part_image = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMFF_io_parts_img)
    part_docum=models.FileField('Файл',upload_to=directory_path_to_OMFF_io_parts_document,null=True,blank=True,)
    def __str__(self):
        return f'{self.name_of_equip}: {self.name_of_part}'

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти к Испытательному оборудованию ОМФФ'


def directory_path_to_OMFF_vo_parts_img(name_of_equipment, invent_number): 
    return 'images/OMFF/VO/parts/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_vo_parts_document(name_of_equipment, invent_number): 
    return 'images/OMFF/VO/parts/document/{0}/{1}'.format(name_of_equipment,invent_number)
class Equip_VO_part_OMFF(models.Model):
    name_of_equip=models.ForeignKey(Equipment_VO_OMFF, on_delete=models.SET_NULL,null=True,related_name='parts')
    name_of_part = models.CharField('Наименование запчасти(расходного материала):', max_length=150, default='')
    fact_number=models.CharField('Заводской номер (расходного материала):', max_length=150, default='')
    part_image = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMFF_vo_parts_img)
    part_docum=models.FileField('Файл',upload_to=directory_path_to_OMFF_vo_parts_document,null=True,blank=True,)
    def __str__(self):
        return f'{self.name_of_equip}: {self.name_of_part}'

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти к Вспомогательному оборудованию ОМФФ'


def directory_path_to_OMFF_voa_parts_img(name_of_equipment, invent_number): 
    return 'images/OMFF/VOA/parts/{0}/{1}'.format(name_of_equipment,invent_number) 
def directory_path_to_OMFF_voa_parts_document(name_of_equipment, invent_number): 
    return 'images/OMFF/VOA/parts/document/{0}/{1}'.format(name_of_equipment,invent_number)        
class Equip_VOA_part_OMFF(models.Model):
    name_of_equip=models.ForeignKey(Equipment_VOA_OMFF, on_delete=models.SET_NULL,null=True,related_name='parts')
    name_of_part = models.CharField('Наименование запчасти(расходного материала):', max_length=150, default='')
    fact_number=models.CharField('Заводской номер (расходного материала):', max_length=150, default='')
    part_image = models.ImageField(null=True,blank=True, upload_to=directory_path_to_OMFF_voa_parts_img)
    part_docum=models.FileField('Файл',upload_to=directory_path_to_OMFF_voa_parts_document,null=True,blank=True,)
    def __str__(self):
        return f'{self.name_of_equip}: {self.name_of_part}'

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти к Оборудованию вне области аккредитации ОМФФ'