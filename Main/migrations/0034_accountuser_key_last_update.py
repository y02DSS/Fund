# Generated by Django 3.2.9 on 2022-11-18 16:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0033_rename_heped_animals_accountuser_helped_animals'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountuser',
            name='key_last_update',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
