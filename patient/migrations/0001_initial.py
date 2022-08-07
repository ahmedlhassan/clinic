# Generated by Django 2.1.5 on 2022-08-06 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phoneNumber', models.CharField(default='0', max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('yORm', models.CharField(blank=True, choices=[('Y', 'Year'), ('M', 'Month')], max_length=1, verbose_name='Y/M')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('patientAddress', models.CharField(max_length=255)),
                ('referredFrom', models.CharField(max_length=200)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='', verbose_name='attachment')),
                ('investigation', models.FileField(blank=True, null=True, upload_to='', verbose_name='investigation')),
                ('note', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
