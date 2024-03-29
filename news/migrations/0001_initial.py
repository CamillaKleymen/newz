import datetime
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
                ('news_title', models.CharField(help_text='here you should enter name of product', max_length=50)),
                ('news_country', models.CharField(max_length=30)),
                ('news_count', models.IntegerField()),
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