# Generated by Django 3.1.6 on 2021-02-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210221_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='sd_volume_max',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Максимальный объем карты памяти'),
        ),
    ]
