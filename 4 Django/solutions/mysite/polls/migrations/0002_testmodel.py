# Generated by Django 2.0.3 on 2018-03-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_models', models.ManyToManyField(related_name='_testmodel_test_models_+', to='polls.TestModel')),
            ],
        ),
    ]