# Generated by Django 4.2.4 on 2023-08-28 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_post_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.FloatField(max_length=10),
        ),
    ]
