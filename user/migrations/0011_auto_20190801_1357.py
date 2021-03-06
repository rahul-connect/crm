# Generated by Django 2.2.2 on 2019-08-01 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0010_center_city'),
        ('user', '0010_auto_20190726_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='center',
        ),
        migrations.AddField(
            model_name='customuser',
            name='select_center',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='enquiry.Center'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('2', 'Counsellor'), ('3', 'Student')], default='2', max_length=2),
        ),
    ]
