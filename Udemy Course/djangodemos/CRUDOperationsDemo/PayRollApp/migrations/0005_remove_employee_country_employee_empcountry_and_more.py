# Generated by Django 5.0.9 on 2024-09-15 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PayRollApp', '0004_country_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Country',
        ),
        migrations.AddField(
            model_name='employee',
            name='EmpCountry',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='PayRollApp.country'),
        ),
        migrations.AddField(
            model_name='employee',
            name='EmpDepartment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='PayRollApp.department'),
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]