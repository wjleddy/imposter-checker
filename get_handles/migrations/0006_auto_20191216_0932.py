# Generated by Django 2.0 on 2019-12-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_handles', '0005_auto_20191215_2243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='similarhandles',
            old_name='base_handle',
            new_name='base_handle_date',
        ),
        migrations.RemoveField(
            model_name='similarhandles',
            name='marked_parody',
        ),
        migrations.AlterField(
            model_name='similarhandles',
            name='bio',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='similarhandles',
            name='date_joined',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='similarhandles',
            name='display_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='similarhandles',
            name='number_following',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='similarhandles',
            name='number_of_followers',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='similarhandles',
            name='number_of_tweets',
            field=models.IntegerField(blank=True),
        ),
    ]
