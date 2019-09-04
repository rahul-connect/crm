# Generated by Django 2.2.2 on 2019-08-01 06:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0008_follow_ups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]