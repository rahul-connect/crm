# Generated by Django 2.2.2 on 2019-07-29 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enquiry', '0003_auto_20190729_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='counsellor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
