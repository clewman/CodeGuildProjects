# Generated by Django 2.0.8 on 2018-10-11 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothek', '0008_auto_20181010_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bibliothek.Author'),
        ),
    ]