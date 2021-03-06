# Generated by Django 3.1.1 on 2020-10-09 03:41

from django.db import migrations, models
import reestr_people.models


class Migration(migrations.Migration):

    dependencies = [
        ('reestr_people', '0003_auto_20201008_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='OMVS_reestr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(default='', max_length=250, verbose_name='Фамилия, имя, отчество')),
                ('job_description', models.CharField(default='', max_length=250, verbose_name='Должность')),
                ('date_settling', models.DateField(verbose_name='Дата трудоустройства')),
                ('dogovor', models.CharField(default='', max_length=250, verbose_name='Основание для привлечения личного труда')),
                ('responsibility', models.CharField(default='', max_length=250, verbose_name='Выполняемые функции, проводые исследования')),
                ('education', models.CharField(default='', max_length=250, verbose_name='Образование')),
                ('experience', models.CharField(default='', max_length=250, verbose_name='Опыт работы')),
                ('attestation_date_protocol', models.CharField(default='', max_length=250, verbose_name='Дата и номер протокола аттестации, периодичность аттестации')),
                ('qualification_up', models.TextField(default='-', verbose_name='Сведения о повышении квалификации')),
                ('date_job_describ', models.DateField(verbose_name='Дата утверждения должностной инструкции')),
                ('group', models.CharField(choices=[('Группа контроля воздуха рабочей зоны', 'Группа контроля воздуха рабочей зоны'), ('Группа по контролю промышленных выбросов и атмосферного воздуха', 'Группа по контролю промышленных выбросов и атмосферного воздуха'), ('В отделе', 'В отделе')], default='-', max_length=250, verbose_name='Наименование группы')),
                ('information', models.CharField(default='', max_length=250, verbose_name='Примечание')),
                ('image_of_person', models.ImageField(blank=True, null=True, upload_to=reestr_people.models.directory_path_to_reestr_personal_OMVS_img)),
            ],
            options={
                'verbose_name': 'Персонал',
                'verbose_name_plural': 'Реестр ОМВС',
            },
        ),
        migrations.AlterField(
            model_name='omvoig_reestr',
            name='group',
            field=models.CharField(choices=[('Группа анализа природных и питьевых вод', 'Группа анализа природных и питьевых вод'), ('Группа хроматографических и спектрометрических исследований', 'Группа хроматографических и спектрометрических исследований'), ('Группа анализа грунтов', 'Группа анализа грунтов'), ('Группа токсикологических исследований', 'Группа токсикологических исследований'), ('В отделе', 'В отделе')], default='', max_length=250, verbose_name='Наименование группы'),
        ),
    ]
