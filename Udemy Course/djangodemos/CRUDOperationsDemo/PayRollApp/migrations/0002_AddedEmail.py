# Generated by Django 5.0.9 on 2024-09-11 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PayRollApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Email',
            field=models.EmailField(default='', max_length=50),
        ),
    ]