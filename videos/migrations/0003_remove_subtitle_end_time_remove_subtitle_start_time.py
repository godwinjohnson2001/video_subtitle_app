# Generated by Django 5.1.1 on 2024-09-19 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_subtitle_end_time_subtitle_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtitle',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='subtitle',
            name='start_time',
        ),
    ]