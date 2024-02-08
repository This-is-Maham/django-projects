# Generated by Django 5.0 on 2024-02-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='firs_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]