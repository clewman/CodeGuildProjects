# Generated by Django 2.0.8 on 2018-10-11 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothek', '0011_auto_20181011_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='check_out',
            field=models.BooleanField(default=True),
        ),
    ]
