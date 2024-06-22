# Generated by Django 4.2.8 on 2024-05-26 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("restapi", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="assignee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="meetingtask",
            name="meeting",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="restapi.meeting"
            ),
        ),
        migrations.AddField(
            model_name="meetingtask",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="restapi.task"
            ),
        ),
        migrations.AddField(
            model_name="meetingattendee",
            name="meeting",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="restapi.meeting"
            ),
        ),
        migrations.AddField(
            model_name="meetingattendee",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="meeting",
            name="recurrence",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="restapi.meetingrecurrence",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="meetingtask",
            unique_together={("meeting", "task")},
        ),
    ]