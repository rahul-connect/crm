# Generated by Django 2.2.2 on 2019-08-08 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0021_auto_20190808_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='trainer',
            field=models.ForeignKey(blank=True, limit_choices_to={'role': '4'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
