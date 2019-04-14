# Generated by Django 2.0.8 on 2018-10-11 17:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothek', '0009_auto_20181011_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bibliothek.Author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 11, 10, 38, 39, 246693), verbose_name='date published'),
            preserve_default=False,
        ),
    ]