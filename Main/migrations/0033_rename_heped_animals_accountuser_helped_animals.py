# Generated by Django 3.2.9 on 2022-11-17 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0032_accountuser_heped_animals'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountuser',
            old_name='heped_animals',
            new_name='helped_animals',
        ),
    ]