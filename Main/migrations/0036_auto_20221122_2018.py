# Generated by Django 3.2.9 on 2022-11-22 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0035_remove_accountuser_key_last_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostanimals',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='collection',
            name='status',
            field=models.CharField(choices=[('В приюте', 'В приюте'), ('Забрали', 'Забрали'), ('Умер', 'Умер'), ('Другая причина', 'Другая причина (описать)')], max_length=200),
        ),
    ]
