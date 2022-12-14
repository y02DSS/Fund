# Generated by Django 3.2.9 on 2022-11-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0015_rename_sheltehotreport_shelterhotreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_animal', models.CharField(max_length=200)),
                ('text_animal', models.TextField(max_length=3000)),
                ('file_animal', models.FileField(upload_to='static/uploads/files/reports')),
            ],
        ),
        migrations.AlterField(
            model_name='collection',
            name='status',
            field=models.CharField(choices=[('В приюте', 'В приюте'), ('Забрали', 'Забрали'), ('Умер', 'Умер'), ('Архив', 'Архив')], max_length=200),
        ),
        migrations.AddField(
            model_name='collection',
            name='animalReport',
            field=models.ManyToManyField(blank=True, null=True, to='Main.AnimalReport'),
        ),
    ]
