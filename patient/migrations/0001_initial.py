# Generated by Django 2.2.15 on 2022-12-29 15:01

from django.db import migrations, models
import django.db.models.deletion
import patient.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cause', '__first__'),
        ('diagnose', '__first__'),
        ('referrer', '__first__'),
        ('treatment', '__first__'),
        ('investigation', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yasser', models.CharField(default='0', max_length=200, null=True)),
                ('name', models.CharField(max_length=255)),
                ('phoneNumber', models.CharField(default='0', max_length=200, null=True)),
                ('birthdate', models.DateField(blank=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('patientAddress', models.CharField(max_length=255, null=True)),
                ('patientComplaint', models.CharField(max_length=255, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cause', models.ManyToManyField(blank=True, to='cause.Cause')),
                ('diagnose', models.ManyToManyField(blank=True, to='diagnose.Diagnose')),
                ('investigation', models.ManyToManyField(blank=True, to='investigation.Investigation')),
                ('referredFrom', models.ManyToManyField(blank=True, to='referrer.Referrer')),
                ('treatment', models.ManyToManyField(blank=True, to='treatment.Treatment')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(blank=True, null=True, upload_to=patient.models.Attachment.content_file_name)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_attachments', to='patient.Patient')),
            ],
        ),
    ]