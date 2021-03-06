# Generated by Django 3.1.1 on 2020-10-12 05:30

from django.db import migrations, models
import django.db.models.deletion
import reestrOMFF.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reestr_people', '0007_auto_20201009_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment_SPI_OMFF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_equipment', models.CharField(default='', max_length=250, verbose_name='Наименование оборудования:')),
                ('image_of_equipment', models.ImageField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_spi_img)),
                ('model_type', models.CharField(default='', max_length=250, verbose_name='Модель, тип:')),
                ('company', models.CharField(default='', max_length=250, verbose_name='Наименование компании производителя')),
                ('factury_number', models.CharField(default='', max_length=250, verbose_name='Заводской Номер:')),
                ('invent_number', models.IntegerField(null=True, verbose_name='Инвентарный номер:')),
                ('date_manufactur', models.CharField(default='', max_length=250, verbose_name='Дата изготовления:')),
                ('date_start_usage', models.CharField(default='', max_length=250, verbose_name='Дата ввода в эксплуатацию:')),
                ('location_lab', models.CharField(default='', max_length=250, verbose_name='Место нахождения (кабинет):')),
                ('date_end_usage', models.CharField(default='', max_length=250, verbose_name='Дата вывода из эксплуатации:')),
                ('reason_of_out', models.CharField(default='', max_length=250, verbose_name='Причина вывода из эксплуатации:')),
                ('fact', models.CharField(default='', max_length=250, verbose_name='Примечание:')),
                ('proof_file', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_spi_proof_file, verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Списанное ЛО ОМФФ',
            },
        ),
        migrations.CreateModel(
            name='Equipment_VU_OMFF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_equipment', models.CharField(default='', max_length=250, verbose_name='Наименование оборудования:')),
                ('image_of_equipment', models.ImageField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_vu_img)),
                ('model_type', models.CharField(default='', max_length=250, verbose_name='Модель, тип:')),
                ('company', models.CharField(default='', max_length=250, verbose_name='Наименование компании производителя')),
                ('factury_number', models.CharField(default='', max_length=250, verbose_name='Заводской Номер:')),
                ('invent_number', models.IntegerField(null=True, verbose_name='Инвентарный номер:')),
                ('date_manufactur', models.CharField(default='', max_length=250, verbose_name='Дата изготовления:')),
                ('date_start_usage', models.CharField(default='', max_length=250, verbose_name='Дата ввода в эксплуатацию:')),
                ('location_lab', models.CharField(default='', max_length=250, verbose_name='Место нахождения (кабинет):')),
                ('date_end_usage', models.CharField(default='', max_length=250, verbose_name='Дата вывода из эксплуатации:')),
                ('reason_of_out', models.CharField(default='', max_length=250, verbose_name='Причина вывода из эксплуатации:')),
                ('fact', models.CharField(default='', max_length=250, verbose_name='Примечание:')),
                ('proof_file', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_vu_proof_file, verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Выведено из эксплуатации ОМФФ',
            },
        ),
        migrations.CreateModel(
            name='Equipment_VOA_OMFF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_equipment', models.CharField(default='', max_length=250, verbose_name='Наименование оборудования:')),
                ('model_type', models.CharField(default='', max_length=250, verbose_name='Модель, тип:')),
                ('number_gosreestr', models.CharField(default='', max_length=250, verbose_name='Номер в госреестре СИ:')),
                ('po', models.CharField(default='', max_length=250, verbose_name='Программное обеспечение')),
                ('company', models.CharField(default='', max_length=250, verbose_name='Наименование компании производителя')),
                ('factury_number', models.CharField(default='', max_length=250, verbose_name='Заводской Номер:')),
                ('invent_number', models.IntegerField(null=True, verbose_name='Инвентарный номер:')),
                ('main_document', models.CharField(default='', max_length=200, verbose_name='Наименование, шифр эксплуатационного документа:')),
                ('date_manufactur', models.CharField(default='', max_length=250, verbose_name='Дата изготовления:')),
                ('date_start_usage', models.CharField(default='', max_length=250, verbose_name='Дата ввода в эксплуатацию:')),
                ('location_lab', models.CharField(default='', max_length=250, verbose_name='Место нахождения (кабинет):')),
                ('microclimate', models.CharField(default='', max_length=250, verbose_name='Условия эксплуатации:')),
                ('range_of_measure', models.CharField(default='', max_length=250, verbose_name='Предел (диапазон) измерений:')),
                ('class_measure', models.CharField(default='', max_length=250, verbose_name='Класс точности, погрешность:')),
                ('organization_check', models.CharField(default='', max_length=250, verbose_name='Организация, выполнившая поверку, калибровку СИ:')),
                ('range_check', models.CharField(default='', max_length=250, verbose_name='Переодичность поверки, калибровки(мес):')),
                ('last_verification', models.CharField(default='', max_length=50, verbose_name='Поверка, аттестация СИ:')),
                ('last_maintaince', models.CharField(default='', max_length=250, verbose_name='Техническое обслужинание, ремонт:')),
                ('tech_condition', models.CharField(default='', max_length=250, verbose_name='Техническое состояние:')),
                ('fact', models.CharField(default='', max_length=250, verbose_name='Примечание:')),
                ('image_of_equipment', models.ImageField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_voa_img)),
                ('verification_file', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_voa_verification, verbose_name='Файл поверки')),
                ('description_type', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_voa_description_type, verbose_name='Описание типа')),
                ('method_file_poverka', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_voa_method_file_poverka, verbose_name='Методика поверки/аттестации')),
                ('responsible_for_use', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reestr_people.omff_reestr')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Вне области аккредитации ОМФФ',
            },
        ),
        migrations.CreateModel(
            name='Equipment_VO_OMFF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_equipment', models.CharField(default='', max_length=150, verbose_name='Наименование оборудования:')),
                ('model_type', models.CharField(default='', max_length=250, verbose_name='Модель, тип:')),
                ('po', models.CharField(default='', max_length=150, verbose_name='Программное обеспечение')),
                ('company', models.CharField(default='', max_length=250, verbose_name='Наименование компании производителя')),
                ('factury_number', models.CharField(default='', max_length=150, verbose_name='Заводской Номер:')),
                ('invent_number', models.IntegerField(null=True, verbose_name='Инвентарный номер:')),
                ('pasport_cto', models.CharField(default='', max_length=200, verbose_name='Паспорт по 174-2011 (дата утверждения):')),
                ('main_document', models.CharField(default='', max_length=200, verbose_name='Наименование, шифр эксплуатационного документа:')),
                ('date_manufactur', models.CharField(default='', max_length=150, verbose_name='Дата изготовления:')),
                ('date_start_usage', models.CharField(default='', max_length=150, verbose_name='Дата ввода в эксплуатацию:')),
                ('location_lab', models.CharField(default='', max_length=150, verbose_name='Место нахождения (кабинет):')),
                ('microclimate', models.CharField(default='', max_length=150, verbose_name='Условия эксплуатации:')),
                ('last_maintaince', models.CharField(default='', max_length=150, verbose_name='Техническое обслужинание, ремонт:')),
                ('tech_condition', models.CharField(default='', max_length=250, verbose_name='Техническое состояние:')),
                ('fact', models.CharField(default='', max_length=250, verbose_name='Примечание:')),
                ('image_of_equipment', models.ImageField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_vo_img)),
                ('verification_file', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_vo_verification, verbose_name='Файл поверки')),
                ('description_type', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_vo_description_type, verbose_name='Описание типа')),
                ('method_file_poverka', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_vo_method_file_poverka, verbose_name='Методика поверки/аттестации')),
                ('responsible_for_use', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reestr_people.omff_reestr')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Вспомогательное оборудование ОМФФ',
            },
        ),
        migrations.CreateModel(
            name='Equipment_SM_OMFF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_equipment', models.CharField(default='', max_length=150, verbose_name='Наименование оборудования:')),
                ('image_of_equipment', models.ImageField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_sm_img)),
                ('model_type', models.CharField(default='', max_length=250, verbose_name='Модель, тип:')),
                ('number_gosreestr', models.CharField(default='', max_length=250, verbose_name='Номер в госреестре СИ:')),
                ('po', models.CharField(default='', max_length=150, verbose_name='Программное обеспечение')),
                ('company', models.CharField(default='', max_length=250, verbose_name='Наименование компании производителя')),
                ('factury_number', models.CharField(default='', max_length=150, verbose_name='Заводской Номер:')),
                ('invent_number', models.IntegerField(null=True, verbose_name='Инвентарный номер:')),
                ('main_document', models.CharField(default='', max_length=200, verbose_name='Наименование, шифр эксплуатационного документа:')),
                ('date_manufactur', models.CharField(default='', max_length=150, verbose_name='Дата изготовления:')),
                ('date_start_usage', models.CharField(default='', max_length=150, verbose_name='Дата ввода в эксплуатацию:')),
                ('location_lab', models.CharField(default='', max_length=150, verbose_name='Место нахождения (кабинет):')),
                ('microclimate', models.CharField(default='', max_length=150, verbose_name='Условия эксплуатации:')),
                ('range_of_measure', models.CharField(default='', max_length=250, verbose_name='Предел (диапазон) измерений:')),
                ('class_measure', models.CharField(default='', max_length=250, verbose_name='Класс точности, погрешность:')),
                ('organization_check', models.CharField(default='', max_length=250, verbose_name='Организация, выполнившая поверку СИ:')),
                ('range_check', models.CharField(default='', max_length=250, verbose_name='Переодичность поверки(мес):')),
                ('last_verification', models.CharField(default='', max_length=50, verbose_name='Поверка СИ:')),
                ('last_maintaince', models.CharField(default='', max_length=150, verbose_name='Техническое обслужинание, ремонт:')),
                ('tech_condition', models.CharField(default='', max_length=250, verbose_name='Техническое состояние:')),
                ('fact', models.CharField(default='', max_length=250, verbose_name='Примечание:')),
                ('responsible_for_use', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reestr_people.omff_reestr')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Стеклянная мера ОМФФ',
            },
        ),
        migrations.CreateModel(
            name='Equipment_SI_OMFF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_equipment', models.CharField(default='', max_length=250, verbose_name='Наименование оборудования:')),
                ('model_type', models.CharField(default='', max_length=250, verbose_name='Модель, тип:')),
                ('number_gosreestr', models.CharField(default='', max_length=250, verbose_name='Номер в госреестре СИ:')),
                ('po', models.CharField(default='', max_length=250, verbose_name='Программное обеспечение')),
                ('company', models.CharField(default='', max_length=250, verbose_name='Наименование компании производителя')),
                ('factury_number', models.CharField(default='', max_length=250, verbose_name='Заводской Номер:')),
                ('invent_number', models.IntegerField(null=True, verbose_name='Инвентарный номер:')),
                ('main_document', models.CharField(default='', max_length=200, verbose_name='Наименование, шифр эксплуатационного документа:')),
                ('date_manufactur', models.CharField(default='', max_length=250, verbose_name='Дата изготовления:')),
                ('date_start_usage', models.CharField(default='', max_length=250, verbose_name='Дата ввода в эксплуатацию:')),
                ('location_lab', models.CharField(default='', max_length=250, verbose_name='Место нахождения (кабинет):')),
                ('microclimate', models.CharField(default='', max_length=250, verbose_name='Условия эксплуатации:')),
                ('range_of_measure', models.CharField(default='', max_length=250, verbose_name='Предел (диапазон) измерений:')),
                ('class_measure', models.CharField(default='', max_length=250, verbose_name='Класс точности, погрешность:')),
                ('organization_check', models.CharField(default='', max_length=250, verbose_name='Организация, выполнившая поверку СИ:')),
                ('range_check', models.CharField(default='', max_length=250, verbose_name='Переодичность поверки(мес):')),
                ('last_verification', models.CharField(default='', max_length=50, verbose_name='Поверка СИ:')),
                ('last_maintaince', models.CharField(default='', max_length=250, verbose_name='Техническое обслужинание, ремонт:')),
                ('tech_condition', models.CharField(default='', max_length=250, verbose_name='Техническое состояние:')),
                ('fact', models.CharField(default='', max_length=250, verbose_name='Примечание:')),
                ('image_of_equipment', models.ImageField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_img)),
                ('verification_file', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_verification, verbose_name='Файл поверки')),
                ('description_type', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_description_type, verbose_name='Описание типа')),
                ('method_file_poverka', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_method_file_poverka, verbose_name='Методика поверки/аттестации')),
                ('responsible_for_use', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reestr_people.omff_reestr')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Средства измерения ОМФФ',
            },
        ),
        migrations.CreateModel(
            name='Equipment_OP_OMFF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_equipment', models.CharField(default='', max_length=150, verbose_name='Наименование оборудования:')),
                ('name_as_passport', models.CharField(default='', max_length=150, verbose_name='Наименование по паспорту:')),
                ('image_of_equipment', models.ImageField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_op_img)),
                ('model_type', models.CharField(default='', max_length=250, verbose_name='Модель, тип:')),
                ('number_gosreestr', models.CharField(default='', max_length=250, verbose_name='Номер в госреестре СИ:')),
                ('po', models.CharField(default='', max_length=150, verbose_name='Программное обеспечение')),
                ('company', models.CharField(default='', max_length=250, verbose_name='Наименование компании производителя')),
                ('pasport_cto', models.CharField(default='', max_length=200, verbose_name='Паспорт по 174-2011 (дата утверждения):')),
                ('factury_number', models.CharField(default='', max_length=150, verbose_name='Заводской Номер:')),
                ('invent_number', models.IntegerField(null=True, verbose_name='Инвентарный номер:')),
                ('main_document', models.CharField(default='', max_length=200, verbose_name='Наименование, шифр эксплуатационного документа:')),
                ('date_get', models.CharField(default='', max_length=150, verbose_name='Дата получения:')),
                ('date_start_usage', models.CharField(default='', max_length=150, verbose_name='Дата ввода в эксплуатацию:')),
                ('location_lab', models.CharField(default='', max_length=150, verbose_name='Место нахождения (кабинет):')),
                ('microclimate', models.CharField(default='', max_length=150, verbose_name='Условия эксплуатации:')),
                ('fact', models.CharField(default='', max_length=250, verbose_name='Примечание:')),
                ('responsible_for_use', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reestr_people.omff_reestr')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Оборудование для отбора проб ОМФФ',
            },
        ),
        migrations.CreateModel(
            name='Equipment_IO_OMFF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_equipment', models.CharField(default='', max_length=150, verbose_name='Наименование оборудования:')),
                ('model_type', models.CharField(default='', max_length=250, verbose_name='Модель, тип:')),
                ('po', models.CharField(default='', max_length=150, verbose_name='Программное обеспечение')),
                ('company', models.CharField(default='', max_length=250, verbose_name='Наименование компании производителя')),
                ('factury_number', models.CharField(default='', max_length=150, verbose_name='Заводской Номер:')),
                ('invent_number', models.IntegerField(null=True, verbose_name='Инвентарный номер:')),
                ('main_document', models.CharField(default='', max_length=200, verbose_name='Наименование, шифр эксплуатационного документа:')),
                ('date_manufactur', models.CharField(default='', max_length=150, verbose_name='Дата изготовления:')),
                ('date_get', models.CharField(default='', max_length=150, verbose_name='Дата получения:')),
                ('date_start_usage', models.CharField(default='', max_length=150, verbose_name='Дата ввода в эксплуатацию:')),
                ('location_lab', models.CharField(default='', max_length=150, verbose_name='Место нахождения (кабинет):')),
                ('microclimate', models.CharField(default='', max_length=150, verbose_name='Условия эксплуатации:')),
                ('organization_check', models.CharField(default='', max_length=150, verbose_name='Организация, выполнившая аттестацию ИО:')),
                ('range_check', models.CharField(default='', max_length=150, verbose_name='Переодичность аттестации(мес):')),
                ('last_verification', models.CharField(default='', max_length=50, verbose_name='Аттестация ИО:')),
                ('last_maintaince', models.CharField(default='', max_length=150, verbose_name='Техническое обслужинание, ремонт:')),
                ('tech_condition', models.CharField(default='', max_length=250, verbose_name='Техническое состояние:')),
                ('fact', models.CharField(default='', max_length=250, verbose_name='Примечание:')),
                ('image_of_equipment', models.ImageField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_io_img)),
                ('verification_file', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_io_verification, verbose_name='Файл поверки')),
                ('description_type', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_io_description_type, verbose_name='Описание типа')),
                ('method_file_poverka', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_io_method_file_poverka, verbose_name='Методика поверки/аттестации')),
                ('responsible_for_use', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reestr_people.omff_reestr')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Испытательное оборудование ОМФФ',
            },
        ),
        migrations.CreateModel(
            name='Equip_VOA_part_OMFF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_part', models.CharField(default='', max_length=150, verbose_name='Наименование запчасти(расходного материала):')),
                ('fact_number', models.CharField(default='', max_length=150, verbose_name='Заводской номер (расходного материала):')),
                ('part_image', models.ImageField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_voa_parts_img)),
                ('part_docum', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_voa_parts_document, verbose_name='Файл')),
                ('name_of_equip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parts', to='reestrOMFF.equipment_voa_omff')),
            ],
            options={
                'verbose_name': 'Запчасти',
                'verbose_name_plural': 'Запчасти к Оборудованию вне области аккредитации ОМФФ',
            },
        ),
        migrations.CreateModel(
            name='Equip_VO_part_OMFF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_part', models.CharField(default='', max_length=150, verbose_name='Наименование запчасти(расходного материала):')),
                ('fact_number', models.CharField(default='', max_length=150, verbose_name='Заводской номер (расходного материала):')),
                ('part_image', models.ImageField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_vo_parts_img)),
                ('part_docum', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_vo_parts_document, verbose_name='Файл')),
                ('name_of_equip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parts', to='reestrOMFF.equipment_vo_omff')),
            ],
            options={
                'verbose_name': 'Запчасти',
                'verbose_name_plural': 'Запчасти к Вспомогательному оборудованию ОМФФ',
            },
        ),
        migrations.CreateModel(
            name='Equip_SI_part_OMFF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_part', models.CharField(default='', max_length=150, verbose_name='Наименование запчасти(расходного материала):')),
                ('fact_number', models.CharField(default='', max_length=150, verbose_name='Заводской номер (расходного материала):')),
                ('part_image', models.ImageField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_c_si_OMFF_parts_img)),
                ('part_docum', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_si_ohti_parts_document, verbose_name='Файл')),
                ('name_of_equip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parts', to='reestrOMFF.equipment_si_omff')),
            ],
            options={
                'verbose_name': 'Запчасти',
                'verbose_name_plural': 'Запчасти к Средствам измерения ОМФФ',
            },
        ),
        migrations.CreateModel(
            name='Equip_IO_part_OMFF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_part', models.CharField(default='', max_length=150, verbose_name='Наименование запчасти(расходного материала):')),
                ('fact_number', models.CharField(default='', max_length=150, verbose_name='Заводской номер (расходного материала):')),
                ('part_image', models.ImageField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_io_parts_img)),
                ('part_docum', models.FileField(blank=True, null=True, upload_to=reestrOMFF.models.directory_path_to_OMFF_io_parts_document, verbose_name='Файл')),
                ('name_of_equip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parts', to='reestrOMFF.equipment_io_omff')),
            ],
            options={
                'verbose_name': 'Запчасти',
                'verbose_name_plural': 'Запчасти к Испытательному оборудованию ОМФФ',
            },
        ),
    ]
