# Generated by Django 3.0.2 on 2020-02-07 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateField(verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateField(verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
