# Generated by Django 3.1.2 on 2021-02-07 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20210207_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='removed',
            field=models.BooleanField(default=False),
        ),
    ]
