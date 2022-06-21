# Generated by Django 4.0.5 on 2022-06-16 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='post category')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='post title')),
                ('excerpt', models.CharField(blank=True, max_length=150, null=True)),
                ('content', models.TextField(verbose_name='post content')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category_posts', to='blog.category')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ['-created'],
            },
        ),
    ]
