# Generated by Django 5.0.2 on 2024-02-16 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_audit', '0003_alter_user_access_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
    ]