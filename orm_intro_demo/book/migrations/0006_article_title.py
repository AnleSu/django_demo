# Generated by Django 3.1.2 on 2021-02-07 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20210207_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
