# Generated by Django 5.1.1 on 2024-09-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtitle',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subtitle',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
