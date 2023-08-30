# Generated by Django 4.2.4 on 2023-08-23 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('body', models.TextField(max_length=500, verbose_name='Содержание')),
                ('date', models.DateField(auto_now_add=True)),
                ('upload_file', models.FileField(null=True, upload_to='./uploads/posts/files/%Y/%m/%d/', verbose_name='Добавить файл (.pdf)')),
                ('upload_img', models.ImageField(null=True, upload_to='./uploads/posts/imgs/%Y/%m/%d/', verbose_name='Добавить изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(max_length=10, verbose_name='Рейтинг')),
            ],
        ),
        migrations.CreateModel(
            name='SubPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minitext', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]