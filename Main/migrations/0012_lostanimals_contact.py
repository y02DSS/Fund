# Generated by Django 3.2.9 on 2022-10-28 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0011_alter_collection_is_take'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostanimals',
            name='contact',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
