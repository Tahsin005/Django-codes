# Generated by Django 5.0.9 on 2024-09-18 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PayRollApp', '0006_alter_employee_empcountry_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartTimeEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('TitleName', models.CharField(max_length=100)),
            ],
        ),
    ]
