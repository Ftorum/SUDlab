# Generated by Django 3.1.1 on 2020-10-11 14:27

from django.db import migrations, models
import reestrOMVOiG.models


class Migration(migrations.Migration):

    dependencies = [
        ('reestrOMVOiG', '0007_equip_vo_part_equip_voa_part'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equip_io_part',
            name='part_docum',
            field=models.FileField(blank=True, null=True, upload_to=reestrOMVOiG.models.directory_path_to_OMVOIG_io_parts_document, verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='equip_io_part',
            name='part_image',
            field=models.ImageField(blank=True, null=True, upload_to=reestrOMVOiG.models.directory_path_to_OMVOIG_io_parts_img),
        ),
        migrations.AlterField(
            model_name='equip_si_part',
            name='part_docum',
            field=models.FileField(blank=True, null=True, upload_to=reestrOMVOiG.models.directory_path_to_OMVOIG_si_parts_document, verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='equip_si_part',
            name='part_image',
            field=models.ImageField(blank=True, null=True, upload_to=reestrOMVOiG.models.directory_path_to_OMVOIG_si_parts_img),
        ),
        migrations.AlterField(
            model_name='equip_vo_part',
            name='part_docum',
            field=models.FileField(blank=True, null=True, upload_to=reestrOMVOiG.models.directory_path_to_OMVOIG_vo_parts_document, verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='equip_vo_part',
            name='part_image',
            field=models.ImageField(blank=True, null=True, upload_to=reestrOMVOiG.models.directory_path_to_OMVOIG_vo_parts_img),
        ),
        migrations.AlterField(
            model_name='equip_voa_part',
            name='part_docum',
            field=models.FileField(blank=True, null=True, upload_to=reestrOMVOiG.models.directory_path_to_OMVOIG_voa_parts_document, verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='equip_voa_part',
            name='part_image',
            field=models.ImageField(blank=True, null=True, upload_to=reestrOMVOiG.models.directory_path_to_OMVOIG_voa_parts_img),
        ),
        migrations.AlterField(
            model_name='equipment_op',
            name='image_of_equipment',
            field=models.ImageField(blank=True, null=True, upload_to=reestrOMVOiG.models.directory_path_to_OMVOIG_op_img),
        ),
        migrations.AlterField(
            model_name='equipment_sm',
            name='image_of_equipment',
            field=models.ImageField(blank=True, null=True, upload_to=reestrOMVOiG.models.directory_path_to_OMVOIG_sm_img),
        ),
        migrations.AlterField(
            model_name='equipment_spi',
            name='image_of_equipment',
            field=models.ImageField(blank=True, null=True, upload_to=reestrOMVOiG.models.directory_path_to_OMVOIG_spi_img),
        ),
        migrations.AlterField(
            model_name='equipment_spi',
            name='proof_file',
            field=models.FileField(blank=True, null=True, upload_to=reestrOMVOiG.models.directory_path_to_OMVOIG_spi_proof_file, verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='equipment_vu',
            name='image_of_equipment',
            field=models.ImageField(blank=True, null=True, upload_to=reestrOMVOiG.models.directory_path_to_OMVOIG_voa_img),
        ),
        migrations.AlterField(
            model_name='equipment_vu',
            name='proof_file',
            field=models.FileField(blank=True, null=True, upload_to=reestrOMVOiG.models.directory_path_to_OMVOIG_vu_proof_file, verbose_name='Файл'),
        ),
    ]
