# Generated by Django 3.0.8 on 2020-07-16 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200716_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='grade',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movies',
            name='postdate',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='subDescription',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
