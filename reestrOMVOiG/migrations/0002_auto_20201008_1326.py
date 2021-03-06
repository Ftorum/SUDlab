# Generated by Django 3.1.1 on 2020-10-08 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reestrOMVOiG', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipment_io',
            options={'verbose_name': 'Оборудование', 'verbose_name_plural': 'Испытательное оборудование ОМВОиГ'},
        ),
        migrations.AlterModelOptions(
            name='equipment_op',
            options={'verbose_name': 'Оборудование', 'verbose_name_plural': 'Оборудование для отбора проб ОМВОиГ'},
        ),
        migrations.AlterModelOptions(
            name='equipment_si',
            options={'verbose_name': 'Оборудование', 'verbose_name_plural': 'Средства измерения ОМВОиГ'},
        ),
        migrations.AlterModelOptions(
            name='equipment_sm',
            options={'verbose_name': 'Оборудование', 'verbose_name_plural': 'Стеклянная мера ОМВОиГ'},
        ),
        migrations.AlterModelOptions(
            name='equipment_spi',
            options={'verbose_name': 'Оборудование', 'verbose_name_plural': 'Списанное ЛО ОМВОиГ'},
        ),
        migrations.AlterModelOptions(
            name='equipment_vo',
            options={'verbose_name': 'Оборудование', 'verbose_name_plural': 'Вспомогательное оборудование ОМВОиГ'},
        ),
        migrations.AlterModelOptions(
            name='equipment_voa',
            options={'verbose_name': 'Оборудование', 'verbose_name_plural': 'Вне области аккредитации ОМВОиГ'},
        ),
        migrations.AlterModelOptions(
            name='equipment_vu',
            options={'verbose_name': 'Оборудование', 'verbose_name_plural': 'Выведено из эксплуатации ОМВОиГ'},
        ),
    ]
