# Generated by Django 4.1 on 2022-08-13 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]