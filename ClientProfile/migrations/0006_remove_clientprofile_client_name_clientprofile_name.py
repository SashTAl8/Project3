# Generated by Django 4.0.3 on 2022-03-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClientProfile', '0005_rename_summary_clientprofile_client_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientprofile',
            name='client_name',
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='Name',
            field=models.CharField(default=None, max_length=120),
        ),
    ]
