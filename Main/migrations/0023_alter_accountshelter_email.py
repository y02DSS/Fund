# Generated by Django 3.2.9 on 2022-11-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0022_alter_collection_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountshelter',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]