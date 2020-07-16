# Generated by Django 3.0.8 on 2020-07-16 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='poster',
        ),
        migrations.AddField(
            model_name='movies',
            name='grade',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movies',
            name='postdate',
            field=models.CharField(default='date published', max_length=20),
        ),
        migrations.AddField(
            model_name='movies',
            name='subDescription',
            field=models.CharField(default='', max_length=50),
        ),
    ]
