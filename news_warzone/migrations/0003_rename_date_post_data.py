# Generated by Django 5.1 on 2024-09-17 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_warzone', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='data',
        ),
    ]
