# Generated by Django 3.2.9 on 2022-10-27 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0009_collection_is_take'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='is_take',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
