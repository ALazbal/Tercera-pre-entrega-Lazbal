# Generated by Django 4.1.5 on 2023-02-03 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_profesor_edad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='cumple',
        ),
        migrations.AlterField(
            model_name='profesor',
            name='edad',
            field=models.IntegerField(),
        ),
    ]