# Generated by Django 3.2.6 on 2021-08-29 22:19

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='profile',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]