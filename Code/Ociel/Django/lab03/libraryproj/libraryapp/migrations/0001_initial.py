# Generated by Django 2.0.3 on 2018-03-24 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Author')),
            ],
        ),
    ]
