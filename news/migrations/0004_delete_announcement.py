# Generated by Django 5.0.3 on 2024-03-14 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_announcement'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Announcement',
        ),
    ]
