# Generated by Django 3.0.8 on 2020-07-16 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200716_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='postdate',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='subDescription',
        ),
    ]