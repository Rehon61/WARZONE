# Generated by Django 5.1 on 2024-09-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_warzone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('date', models.JSONField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
