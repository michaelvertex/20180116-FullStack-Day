# Generated by Django 2.0.3 on 2018-03-13 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_remove_task_finished_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='finished_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]