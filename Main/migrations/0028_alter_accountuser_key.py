# Generated by Django 3.2.9 on 2022-11-17 15:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0027_alter_accountuser_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='key',
            field=models.CharField(default=uuid.uuid4, max_length=50, primary_key=True, serialize=False),
        ),
    ]
