# Generated by Django 2.0.8 on 2018-10-10 19:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bibliothek', '0004_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Circulation',
            new_name='Book',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
