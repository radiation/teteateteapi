# Generated by Django 4.2.8 on 2023-12-23 17:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_eventtime_userpreferences_remove_agendaitem_meeting_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingtask',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]