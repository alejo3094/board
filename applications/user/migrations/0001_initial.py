# Generated by Django 2.2 on 2019-04-27 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_id', models.CharField(choices=[('CC', 'Cedula de ciudadania'), ('TI', 'Tarjeta de identidad'), ('CE', 'Cedula de extranjería')], max_length=30, verbose_name='type_id')),
                ('id_number', models.CharField(max_length=30, verbose_name='identification')),
                ('picture', models.ImageField(upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
