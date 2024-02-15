# Generated by Django 5.0.2 on 2024-02-15 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(max_length=50, verbose_name='Account No')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('balance', models.FloatField(verbose_name='Balance')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'db_table': 'account',
                'ordering': ['-account_no'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('address', models.TextField(verbose_name='Address')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('login', models.EmailField(max_length=254, verbose_name='Login')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('access_type', models.CharField(choices=[('user', 'User'), ('customer', 'Customer')], max_length=30, verbose_name='Access')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50, unique=True, verbose_name='Reference')),
                ('description', models.TextField(verbose_name='Description')),
                ('old_balance', models.FloatField(verbose_name='Old balance')),
                ('new_balance', models.FloatField(verbose_name='New balance')),
                ('state', models.CharField(choices=[('draft', 'Draft'), ('valid', 'Valid'), ('cancel', 'Cancel')], max_length=20, verbose_name='State')),
                ('customer_id', models.SmallIntegerField(verbose_name='Customer ID')),
                ('action', models.CharField(max_length=15, verbose_name='Action')),
                ('write_date', models.DateTimeField(auto_now=True, verbose_name='Write date')),
                ('write_id', models.SmallIntegerField(verbose_name='Write ID')),
                ('account_ids', models.ManyToManyField(to='account_audit.account', verbose_name='Accounts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account_audit.user', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Audit',
                'verbose_name_plural': 'Audits',
                'db_table': 'audit',
                'ordering': ['-write_date'],
            },
        ),
        migrations.AddField(
            model_name='account',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account_audit.user', verbose_name='Customer'),
        ),
    ]
