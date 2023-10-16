# Generated by Django 4.2.4 on 2023-10-12 21:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='saved_by',
            field=models.ManyToManyField(related_name='saved_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]