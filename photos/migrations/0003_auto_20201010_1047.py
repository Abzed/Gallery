# Generated by Django 3.1.2 on 2020-10-10 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20201010_1041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='tags',
            new_name='location',
        ),
    ]
