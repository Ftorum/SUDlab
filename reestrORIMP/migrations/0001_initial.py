# Generated by Django 3.1.1 on 2020-10-12 08:39

from django.db import migrations, models
import django.db.models.deletion
import reestrORIMP.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reestr_people', '0007_auto_20201009_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment_ET_ORIMP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(default='', max_length=250, verbose_name='Регистрационный номер эталона:')),
                ('name_of_equipment_passport', models.CharField(default='', max_length=250, verbose_name='Наименование оборудования по паспорту:')),
                ('name_of_equipment_measure', models.CharField(default='', max_length=250, verbose_name='Наименование средств измерений:')),
                ('factury_number', models.CharField(default='', max_length=250, verbose_name='Заводской Номер:')),
                ('main_document', models.CharField(default='', max_length=200, verbose_name='Приказ об утверждени эталонов единиц величин:')),
                ('fact', models.CharField(default='', max_length=250, verbose_name='Примечание:')),
                ('image_of_equipment', models.ImageField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_et_img)),
                ('verification_file', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_et_verification, verbose_name='Файл поверки')),
                ('description_type', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_et_description_type, verbose_name='Описание типа')),
                ('method_file_poverka', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_et_method_file_poverka, verbose_name='Методика поверки/аттестации')),
            ],
            options={
                'verbose_name': 'Эталон',
                'verbose_name_plural': 'Перечень эталонов ОРиМР',
            },
        ),
        migrations.CreateModel(
            name='Equipment_RET_ORIMP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(default='', max_length=250, verbose_name='Регистрационный номер эталона:')),
                ('name_of_equipment_passport', models.CharField(default='', max_length=250, verbose_name='Наименование оборудования по паспорту:')),
                ('name_of_equipment_measure', models.CharField(default='', max_length=250, verbose_name='Наименование средств измерений:')),
                ('factury_number', models.CharField(default='', max_length=250, verbose_name='Заводской Номер:')),
                ('fact', models.CharField(default='', max_length=250, verbose_name='Примечание:')),
                ('numb_elect_zayavki', models.CharField(default='', max_length=250, verbose_name='Номер электронной заявки:')),
                ('date_next_verification', models.CharField(default='', max_length=250, verbose_name='Дата следующей поверки:')),
                ('date_attestation_et', models.CharField(default='', max_length=250, verbose_name='Дата аттестации элатона:')),
                ('scheme_of_verivication', models.TextField(default='', max_length=250, verbose_name='Наименование Государственной поверочной схемы для средств измерений:')),
                ('image_of_equipment', models.ImageField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_ret_img)),
                ('verification_file', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_ret_verification, verbose_name='Файл поверки')),
                ('description_type', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_ret_description_type, verbose_name='Описание типа')),
                ('method_file_poverka', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_ret_method_file_poverka, verbose_name='Методика поверки/аттестации')),
            ],
            options={
                'verbose_name': 'Эталон',
                'verbose_name_plural': 'Реестр эталонов ОРиМР',
            },
        ),
        migrations.CreateModel(
            name='Equipment_VO_ORIMP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_equipment_passport', models.CharField(default='', max_length=250, verbose_name='Наименование оборудования по паспорту:')),
                ('name_of_equipment_gos_reestr', models.CharField(default='', max_length=250, verbose_name='Наименование оборудования по госреестру:')),
                ('equip_R3', models.CharField(default='', max_length=250, verbose_name='Наименование оборудования R3:')),
                ('model_type', models.CharField(default='', max_length=250, verbose_name='Модель, тип:')),
                ('number_gosreestr', models.CharField(default='', max_length=250, verbose_name='Номер в госреестре СИ:')),
                ('number_etalon', models.CharField(default='', max_length=250, verbose_name='Регистрационный номер эталона:')),
                ('po', models.CharField(default='', max_length=250, verbose_name='Программное обеспечение')),
                ('company', models.CharField(default='', max_length=250, verbose_name='Наименование компании производителя')),
                ('factury_number', models.CharField(default='', max_length=250, verbose_name='Заводской Номер:')),
                ('invent_number', models.IntegerField(null=True, verbose_name='Инвентарный номер:')),
                ('main_document', models.CharField(default='', max_length=200, verbose_name='Наименование, шифр эксплуатационного документа:')),
                ('range_of_measure', models.CharField(default='', max_length=250, verbose_name='Предел (диапазон) измерений:')),
                ('class_measure', models.CharField(default='', max_length=250, verbose_name='Класс точности, погрешность:')),
                ('location_lab', models.CharField(default='', max_length=250, verbose_name='Место нахождения (кабинет):')),
                ('microclimate', models.CharField(default='', max_length=250, verbose_name='Условия эксплуатации:')),
                ('organization_check', models.CharField(default='', max_length=250, verbose_name='Организация, выполнившая поверку СИ:')),
                ('range_check', models.CharField(default='', max_length=250, verbose_name='Переодичность поверки(мес):')),
                ('last_verification', models.CharField(default='', max_length=50, verbose_name='Поверка СИ:')),
                ('next_verification', models.CharField(default='', max_length=50, verbose_name='Дата следующей поверки/калибровки/аттестации:')),
                ('last_maintaince', models.CharField(default='', max_length=250, verbose_name='Техническое обслужинание, ремонт:')),
                ('tech_condition', models.CharField(default='', max_length=250, verbose_name='Техническое состояние:')),
                ('date_manufactur', models.CharField(default='', max_length=250, verbose_name='Дата изготовления:')),
                ('date_start_usage', models.CharField(default='', max_length=250, verbose_name='Дата ввода в эксплуатацию:')),
                ('fact', models.CharField(default='', max_length=250, verbose_name='Примечание:')),
                ('image_of_equipment', models.ImageField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_vo_img)),
                ('verification_file', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_vo_verification, verbose_name='Файл поверки')),
                ('description_type', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_vo_description_type, verbose_name='Описание типа')),
                ('method_file_poverka', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_vo_method_file_poverka, verbose_name='Методика поверки/аттестации')),
                ('responsible_for_use', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reestr_people.omvs_reestr')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Вспомогательное оборудование ОРиМР',
            },
        ),
        migrations.CreateModel(
            name='Equipment_SI_ORIMP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_equipment_passport', models.CharField(default='', max_length=250, verbose_name='Наименование оборудования по паспорту:')),
                ('name_of_equipment_gos_reestr', models.CharField(default='', max_length=250, verbose_name='Наименование оборудования по госреестру:')),
                ('equip_R3', models.CharField(default='', max_length=250, verbose_name='Наименование оборудования R3:')),
                ('model_type', models.CharField(default='', max_length=250, verbose_name='Модель, тип:')),
                ('number_gosreestr', models.CharField(default='', max_length=250, verbose_name='Номер в госреестре СИ:')),
                ('number_etalon', models.CharField(default='', max_length=250, verbose_name='Регистрационный номер эталона:')),
                ('po', models.CharField(default='', max_length=250, verbose_name='Программное обеспечение')),
                ('company', models.CharField(default='', max_length=250, verbose_name='Наименование компании производителя')),
                ('factury_number', models.CharField(default='', max_length=250, verbose_name='Заводской Номер:')),
                ('invent_number', models.IntegerField(null=True, verbose_name='Инвентарный номер:')),
                ('main_document', models.CharField(default='', max_length=200, verbose_name='Наименование, шифр эксплуатационного документа:')),
                ('range_of_measure', models.CharField(default='', max_length=250, verbose_name='Предел (диапазон) измерений:')),
                ('class_measure', models.CharField(default='', max_length=250, verbose_name='Класс точности, погрешность:')),
                ('location_lab', models.CharField(default='', max_length=250, verbose_name='Место нахождения (кабинет):')),
                ('microclimate', models.CharField(default='', max_length=250, verbose_name='Условия эксплуатации:')),
                ('organization_check', models.CharField(default='', max_length=250, verbose_name='Организация, выполнившая поверку СИ:')),
                ('range_check', models.CharField(default='', max_length=250, verbose_name='Переодичность поверки(мес):')),
                ('last_verification', models.CharField(default='', max_length=50, verbose_name='Поверка СИ:')),
                ('next_verification', models.CharField(default='', max_length=50, verbose_name='Дата следующей поверки/калибровки/аттестации:')),
                ('last_maintaince', models.CharField(default='', max_length=250, verbose_name='Техническое обслужинание, ремонт:')),
                ('tech_condition', models.CharField(default='', max_length=250, verbose_name='Техническое состояние:')),
                ('date_manufactur', models.CharField(default='', max_length=250, verbose_name='Дата изготовления:')),
                ('date_start_usage', models.CharField(default='', max_length=250, verbose_name='Дата ввода в эксплуатацию:')),
                ('fact', models.CharField(default='', max_length=250, verbose_name='Примечание:')),
                ('image_of_equipment', models.ImageField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_img)),
                ('verification_file', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_verification, verbose_name='Файл поверки')),
                ('description_type', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_description_type, verbose_name='Описание типа')),
                ('method_file_poverka', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_method_file_poverka, verbose_name='Методика поверки/аттестации')),
                ('responsible_for_use', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reestr_people.omvs_reestr')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Средства измерения ОРиМР',
            },
        ),
        migrations.CreateModel(
            name='Equipment_IO_ORIMP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_equipment_passport', models.CharField(default='', max_length=250, verbose_name='Наименование оборудования по паспорту:')),
                ('name_of_equipment_gos_reestr', models.CharField(default='', max_length=250, verbose_name='Наименование оборудования по госреестру:')),
                ('equip_R3', models.CharField(default='', max_length=250, verbose_name='Наименование оборудования R3:')),
                ('model_type', models.CharField(default='', max_length=250, verbose_name='Модель, тип:')),
                ('number_gosreestr', models.CharField(default='', max_length=250, verbose_name='Номер в госреестре СИ:')),
                ('number_etalon', models.CharField(default='', max_length=250, verbose_name='Регистрационный номер эталона:')),
                ('po', models.CharField(default='', max_length=250, verbose_name='Программное обеспечение')),
                ('company', models.CharField(default='', max_length=250, verbose_name='Наименование компании производителя')),
                ('factury_number', models.CharField(default='', max_length=250, verbose_name='Заводской Номер:')),
                ('invent_number', models.IntegerField(null=True, verbose_name='Инвентарный номер:')),
                ('main_document', models.CharField(default='', max_length=200, verbose_name='Наименование, шифр эксплуатационного документа:')),
                ('range_of_measure', models.CharField(default='', max_length=250, verbose_name='Предел (диапазон) измерений:')),
                ('class_measure', models.CharField(default='', max_length=250, verbose_name='Класс точности, погрешность:')),
                ('location_lab', models.CharField(default='', max_length=250, verbose_name='Место нахождения (кабинет):')),
                ('microclimate', models.CharField(default='', max_length=250, verbose_name='Условия эксплуатации:')),
                ('organization_check', models.CharField(default='', max_length=250, verbose_name='Организация, выполнившая поверку СИ:')),
                ('range_check', models.CharField(default='', max_length=250, verbose_name='Переодичность поверки(мес):')),
                ('last_verification', models.CharField(default='', max_length=50, verbose_name='Поверка СИ:')),
                ('next_verification', models.CharField(default='', max_length=50, verbose_name='Дата следующей поверки/калибровки/аттестации:')),
                ('last_maintaince', models.CharField(default='', max_length=250, verbose_name='Техническое обслужинание, ремонт:')),
                ('tech_condition', models.CharField(default='', max_length=250, verbose_name='Техническое состояние:')),
                ('date_manufactur', models.CharField(default='', max_length=250, verbose_name='Дата изготовления:')),
                ('date_start_usage', models.CharField(default='', max_length=250, verbose_name='Дата ввода в эксплуатацию:')),
                ('fact', models.CharField(default='', max_length=250, verbose_name='Примечание:')),
                ('image_of_equipment', models.ImageField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_io_img)),
                ('verification_file', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_io_verification, verbose_name='Файл поверки')),
                ('description_type', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_io_description_type, verbose_name='Описание типа')),
                ('method_file_poverka', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_io_method_file_poverka, verbose_name='Методика поверки/аттестации')),
                ('responsible_for_use', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reestr_people.omvs_reestr')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Испытательное оборудование ОРиМР',
            },
        ),
        migrations.CreateModel(
            name='Equip_VO_part_ORIMP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_part', models.CharField(default='', max_length=150, verbose_name='Наименование запчасти(расходного материала):')),
                ('fact_number', models.CharField(default='', max_length=150, verbose_name='Заводской номер (расходного материала):')),
                ('part_image', models.ImageField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_vo_parts_img)),
                ('part_docum', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_vo_parts_document, verbose_name='Файл')),
                ('name_of_equip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parts', to='reestrORIMP.equipment_vo_orimp')),
            ],
            options={
                'verbose_name': 'Запчасти',
                'verbose_name_plural': 'Запчасти к Вспомогательному оборудованию ОРиМР',
            },
        ),
        migrations.CreateModel(
            name='Equip_SI_part_ORIMP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_part', models.CharField(default='', max_length=150, verbose_name='Наименование запчасти(расходного материала):')),
                ('fact_number', models.CharField(default='', max_length=150, verbose_name='Заводской номер (расходного материала):')),
                ('part_image', models.ImageField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_c_si_ORIMP_parts_img)),
                ('part_docum', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_si_ohti_parts_document, verbose_name='Файл')),
                ('name_of_equip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parts', to='reestrORIMP.equipment_si_orimp')),
            ],
            options={
                'verbose_name': 'Запчасти',
                'verbose_name_plural': 'Запчасти к Средствам измерения ОРиМР',
            },
        ),
        migrations.CreateModel(
            name='Equip_IO_part_ORIMP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_part', models.CharField(default='', max_length=150, verbose_name='Наименование запчасти(расходного материала):')),
                ('fact_number', models.CharField(default='', max_length=150, verbose_name='Заводской номер (расходного материала):')),
                ('part_image', models.ImageField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_io_parts_img)),
                ('part_docum', models.FileField(blank=True, null=True, upload_to=reestrORIMP.models.directory_path_to_ORIMP_io_parts_document, verbose_name='Файл')),
                ('name_of_equip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parts', to='reestrORIMP.equipment_io_orimp')),
            ],
            options={
                'verbose_name': 'Запчасти',
                'verbose_name_plural': 'Запчасти к Испытательному оборудованию ОРиМР',
            },
        ),
    ]
