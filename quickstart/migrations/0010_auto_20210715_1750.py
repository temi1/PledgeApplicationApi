# Generated by Django 3.2.4 on 2021-07-15 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0009_alter_userpledge_pledge'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpledge',
            name='author',
            field=models.CharField(default='Def', max_length=500),
        ),
        migrations.AlterField(
            model_name='userpledge',
            name='pledge',
            field=models.IntegerField(default=0),
        ),
    ]
