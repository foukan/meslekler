# Generated by Django 2.2.17 on 2020-12-27 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201227_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='body',
        ),
    ]