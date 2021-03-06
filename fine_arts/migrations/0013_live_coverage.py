# Generated by Django 3.1.2 on 2021-02-25 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fine_arts', '0012_auto_20210224_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='live_coverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporter_name', models.CharField(max_length=250)),
                ('channel_name', models.CharField(max_length=250)),
                ('heading', models.CharField(max_length=1000)),
                ('video1', models.FileField(upload_to='live_coverage')),
                ('vedio_details', models.CharField(max_length=100000)),
            ],
        ),
    ]
