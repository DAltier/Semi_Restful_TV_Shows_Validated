# Generated by Django 2.2.4 on 2021-04-22 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0003_auto_20210421_1902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='desc',
            new_name='description',
        ),
    ]
