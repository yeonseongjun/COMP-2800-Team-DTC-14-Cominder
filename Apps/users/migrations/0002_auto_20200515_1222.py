# Generated by Django 3.0.5 on 2020-05-15 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='end',
            field=models.IntegerField(blank=True, default=8, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='start',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
