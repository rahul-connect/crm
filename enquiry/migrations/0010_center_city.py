# Generated by Django 2.2.2 on 2019-08-01 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0009_center_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enquiry.City'),
            preserve_default=False,
        ),
    ]
