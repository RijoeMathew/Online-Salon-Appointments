# Generated by Django 4.1.3 on 2022-11-07 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('post_title', models.CharField(max_length=200)),
                ('post_content', models.TextField(default='tutorial content')),
                ('date_published', models.DateField(blank=True, null=True)),
                ('user_profile_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
