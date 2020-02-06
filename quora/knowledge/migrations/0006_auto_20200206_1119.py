# Generated by Django 3.0.2 on 2020-02-06 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0005_auto_20200206_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
