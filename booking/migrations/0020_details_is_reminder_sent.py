# Generated by Django 4.1.3 on 2022-11-27 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0019_services_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='is_reminder_sent',
            field=models.IntegerField(default=0),
        ),
    ]