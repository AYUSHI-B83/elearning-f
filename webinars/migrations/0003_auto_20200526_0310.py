# Generated by Django 2.2 on 2020-05-25 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webinars', '0002_fileupload_gdlink_textblock_ytlink'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FileUpload',
            new_name='FileUploadW',
        ),
        migrations.RenameModel(
            old_name='gdlink',
            new_name='gdlinkW',
        ),
        migrations.RenameModel(
            old_name='TextBlock',
            new_name='TextBlockW',
        ),
        migrations.RenameModel(
            old_name='YTLink',
            new_name='YTLinkW',
        ),
    ]
