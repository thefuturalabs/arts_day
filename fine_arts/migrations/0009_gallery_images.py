# Generated by Django 3.1.2 on 2021-02-22 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fine_arts', '0008_auto_20210222_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='gallery_images')),
                ('image2', models.ImageField(upload_to='gallery_images')),
                ('image3', models.ImageField(upload_to='gallery_images')),
                ('image4', models.ImageField(upload_to='gallery_images')),
                ('image5', models.ImageField(upload_to='gallery_images')),
                ('image6', models.ImageField(upload_to='gallery_images')),
                ('image7', models.ImageField(upload_to='gallery_images')),
                ('image8', models.ImageField(upload_to='gallery_images')),
            ],
        ),
    ]
