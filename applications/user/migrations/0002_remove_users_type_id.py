# Generated by Django 2.2 on 2019-04-28 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='type_id',
        ),
    ]
