# Generated by Django 3.2.4 on 2021-07-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0006_rename_name_pledgefeed_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledgefeed',
            name='photo',
            field=models.TextField(),
        ),
    ]
