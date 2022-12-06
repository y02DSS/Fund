# Generated by Django 3.2.9 on 2022-12-06 13:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0040_auto_20221205_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelteraccount',
            name='about',
            field=models.TextField(blank=True, default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shelteraccount',
            name='address',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shelteraccount',
            name='contact',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shelteraccount',
            name='date_visits',
            field=models.TextField(blank=True, default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shelteraccount',
            name='director_name',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shelteraccount',
            name='hotReport',
            field=models.ManyToManyField(blank=True, to='Main.ShelterHotReport'),
        ),
        migrations.AlterField(
            model_name='shelteraccount',
            name='logo',
            field=models.FileField(blank=True, default=django.utils.timezone.now, upload_to='static/img/accounts'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shelteraccount',
            name='news',
            field=models.ManyToManyField(blank=True, to='Main.ShelterNews'),
        ),
        migrations.AlterField(
            model_name='shelteraccount',
            name='requisites',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shelteraccount',
            name='social_network',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
