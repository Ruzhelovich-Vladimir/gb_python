# Generated by Django 3.0.3 on 2020-03-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0002_auto_20200308_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='delivery_at',
            field=models.DateField(verbose_name='Дата поступления'),
        ),
    ]
