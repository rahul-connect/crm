# Generated by Django 2.2.2 on 2019-07-25 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_delete_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('0', 'Counsellor'), ('1', 'Student')], default='0', max_length=2),
        ),
    ]
