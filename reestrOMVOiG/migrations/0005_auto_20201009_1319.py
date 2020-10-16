# Generated by Django 3.1.1 on 2020-10-09 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reestr_people', '0007_auto_20201009_1319'),
        ('reestrOMVOiG', '0004_auto_20201009_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment_io',
            name='responsible_for_use',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reestr_people.omvoig_reestr'),
        ),
        migrations.AlterField(
            model_name='equipment_op',
            name='responsible_for_use',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reestr_people.omvoig_reestr'),
        ),
        migrations.AlterField(
            model_name='equipment_sm',
            name='responsible_for_use',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reestr_people.omvoig_reestr'),
        ),
        migrations.AlterField(
            model_name='equipment_vo',
            name='responsible_for_use',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reestr_people.omvoig_reestr'),
        ),
        migrations.AlterField(
            model_name='equipment_voa',
            name='responsible_for_use',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reestr_people.omvoig_reestr'),
        ),
    ]