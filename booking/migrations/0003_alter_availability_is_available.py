# Generated by Django 4.1.3 on 2022-11-18 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='is_available',
            field=models.SmallIntegerField(default=1),
        ),
    ]