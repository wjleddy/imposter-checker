# Generated by Django 3.0 on 2019-12-15 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseHandle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(max_length=15, unique_for_date='date_pulled')),
                ('date_pulled', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SimilarHandles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(max_length=15)),
                ('suspended', models.BooleanField()),
                ('display_name', models.CharField(max_length=50)),
                ('number_of_tweets', models.IntegerField()),
                ('number_of_followers', models.IntegerField()),
                ('number_following', models.IntegerField()),
                ('marked_parody', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('bio', models.CharField(max_length=160)),
                ('base_handle_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_handles.BaseHandle')),
            ],
        ),
    ]
