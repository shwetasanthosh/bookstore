# Generated by Django 4.1.2 on 2022-11-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('author', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('pages', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]