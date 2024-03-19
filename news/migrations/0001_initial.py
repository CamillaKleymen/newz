<<<<<<< HEAD
# Generated by Django 5.0.3 on 2024-03-18 17:06

import datetime
=======
# Generated by Django 5.0.3 on 2024-03-13 14:12

>>>>>>> 77ced790e329732b33d64c36c9ac7bb45d3f7198
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'News category',
                'verbose_name_plural': 'News categories',
            },
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('news_title', models.CharField(max_length=50)),
                ('news_country', models.CharField(max_length=30)),
                ('news_date', models.DateField(default=datetime.date)),
=======
                ('news_title', models.CharField(help_text='here you should enter name of product', max_length=50)),
                ('news_country', models.CharField(max_length=30)),
                ('news_count', models.IntegerField()),
>>>>>>> 77ced790e329732b33d64c36c9ac7bb45d3f7198
                ('news_description', models.TextField()),
                ('news_image', models.FileField(upload_to='news_images')),
                ('news_created_at', models.DateTimeField(auto_now_add=True)),
                ('news_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.categorymodel')),
            ],
            options={
                'verbose_name': 'Announcement',
                'verbose_name_plural': 'News',
            },
        ),
    ]
