# Generated by Django 2.2 on 2020-05-11 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_tasklist_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
