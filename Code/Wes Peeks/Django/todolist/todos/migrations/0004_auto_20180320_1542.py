# Generated by Django 2.0.3 on 2018-03-20 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20180320_1542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ['title']},
        ),
    ]
