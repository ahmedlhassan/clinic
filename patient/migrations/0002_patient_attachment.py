# Generated by Django 2.1.5 on 2022-08-04 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='attachment'),
        ),
    ]
