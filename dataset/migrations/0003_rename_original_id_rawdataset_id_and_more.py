# Generated by Django 4.1.7 on 2023-05-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dataset", "0002_remove_rawdataset_compressed_file"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rawdataset",
            old_name="original_id",
            new_name="id",
        ),
        migrations.AlterField(
            model_name="rawdataset",
            name="version_id",
            field=models.IntegerField(default=0),
        ),
    ]
