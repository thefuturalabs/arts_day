# Generated by Django 3.1.2 on 2021-02-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fine_arts', '0009_gallery_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='score_board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group1_score', models.IntegerField()),
                ('group2_score', models.IntegerField()),
                ('group3_score', models.IntegerField()),
                ('group4_score', models.IntegerField()),
                ('group5_score', models.IntegerField()),
                ('group6_score', models.IntegerField()),
            ],
        ),
    ]