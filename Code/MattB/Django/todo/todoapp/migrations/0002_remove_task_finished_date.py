# Generated by Django 2.0.3 on 2018-03-13 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='finished_date',
        ),
    ]
