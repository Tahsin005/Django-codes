# Generated by Django 4.2.10 on 2024-04-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=70)),
                ('stuemail', models.EmailField(max_length=70)),
                ('stupass', models.CharField(max_length=70)),
            ],
        ),
    ]
