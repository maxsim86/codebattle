# Generated by Django 4.1.2 on 2022-10-12 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_event_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hackathon_participant',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
