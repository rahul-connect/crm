# Generated by Django 2.2.2 on 2019-08-05 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0012_auto_20190801_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='course_fee',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='starting_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
