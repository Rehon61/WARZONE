# Generated by Django 5.1 on 2024-09-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_warzone', '0003_rename_date_post_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
