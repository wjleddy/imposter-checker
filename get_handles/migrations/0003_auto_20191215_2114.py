# Generated by Django 2.2.8 on 2019-12-16 05:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('get_handles', '0002_auto_20191215_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='similarhandles',
            name='date_pulled',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
