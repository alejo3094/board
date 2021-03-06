# Generated by Django 2.2 on 2019-04-28 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='contenidoNota')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Board')),
                ('userCreator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Users')),
            ],
        ),
    ]
