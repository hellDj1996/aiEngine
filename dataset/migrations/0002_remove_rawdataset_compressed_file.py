# Generated by Django 4.1.7 on 2023-05-12 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dataset", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rawdataset",
            name="compressed_file",
        ),
    ]
