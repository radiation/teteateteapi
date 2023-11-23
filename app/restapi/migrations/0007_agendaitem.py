# Generated by Django 4.2.7 on 2023-11-23 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0004_user_user_name_alter_user_email_address_squashed_0006_meeting_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agendaitems_meeting_related', to='restapi.meeting')),
            ],
        ),
    ]