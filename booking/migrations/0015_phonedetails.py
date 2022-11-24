# Generated by Django 4.1.3 on 2022-11-24 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_alter_details_cancel_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='phonedetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('phone', models.IntegerField(max_length=10)),
            ],
            options={
                'ordering': ['username'],
            },
        ),
    ]
