# Generated by Django 5.1.1 on 2024-09-08 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video_file', models.FileField(upload_to='videos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subtitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(default='English', max_length=50)),
                ('content', models.TextField()),
                ('subtitle_file', models.FileField(blank=True, null=True, upload_to='subtitles/')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtitles', to='videos.video')),
            ],
        ),
    ]