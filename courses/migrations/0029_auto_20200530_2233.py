# Generated by Django 2.2 on 2020-05-30 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0028_auto_20200530_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.IntegerField(default=0, max_length=20, null=True),
        ),

    ]
