# Generated by Django 3.1.6 on 2021-03-08 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210308_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productfeaturevalidators',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productfeaturevalidators',
            name='feature',
        ),
        migrations.DeleteModel(
            name='ProductFeatures',
        ),
        migrations.DeleteModel(
            name='ProductFeatureValidators',
        ),
    ]
