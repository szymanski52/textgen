# Generated by Django 2.2.3 on 2019-07-30 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsmanager', '0003_auto_20190729_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='privategoal',
            name='goalPriority',
            field=models.IntegerField(default=1),
        ),
    ]
