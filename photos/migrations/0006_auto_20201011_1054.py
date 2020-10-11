# Generated by Django 3.1.2 on 2020-10-11 10:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_auto_20201010_1108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ManyToManyField(to='photos.Location'),
        ),
    ]
