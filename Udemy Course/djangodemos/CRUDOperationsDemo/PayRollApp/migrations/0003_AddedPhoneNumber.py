# Generated by Django 5.0.9 on 2024-09-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PayRollApp', '0002_AddedEmail'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='PhoneNumber',
            field=models.CharField(default='', max_length=100),
        ),
    ]
