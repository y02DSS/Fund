# Generated by Django 3.2.9 on 2022-10-27 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0010_alter_collection_is_take'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='is_take',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
