# Generated by Django 2.1.5 on 2022-08-04 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_auto_20220804_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='yORm',
            field=models.CharField(blank=True, choices=[('Y', 'Year'), ('M', 'Month')], max_length=1, verbose_name='Y/M'),
        ),
    ]
