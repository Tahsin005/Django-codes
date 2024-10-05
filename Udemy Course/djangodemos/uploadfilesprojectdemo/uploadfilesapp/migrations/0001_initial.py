# Generated by Django 5.0.9 on 2024-10-05 10:56

import django.db.models.deletion
import uploadfilesapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('cv_file', models.FileField(blank=True, null=True, upload_to='employee_files/cv/')),
                ('photo_file', models.FileField(blank=True, null=True, upload_to='employee_files/photo/')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_file', models.FileField(blank=True, null=True, upload_to=uploadfilesapp.models.certificate_upload_path)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploadfilesapp.employee')),
            ],
        ),
    ]
