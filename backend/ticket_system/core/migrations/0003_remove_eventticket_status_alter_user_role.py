# Generated by Django 5.2.1 on 2025-06-21 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_event_eventstats_eventticket_delete_test_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventticket',
            name='status',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('organizer', 'Organizer'), ('admin', 'Admin'), ('visitor', 'Visitor')], default='admin', max_length=20),
        ),
    ]
