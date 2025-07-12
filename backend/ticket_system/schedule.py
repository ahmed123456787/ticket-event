from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

schedule, _ = IntervalSchedule.objects.get_or_create(
    every=1,
    period=IntervalSchedule.MINUTES
)


task_name = 'send event reminders'
if not PeriodicTask.objects.filter(name=task_name).exists():
    # Create the task with required arguments as positional args
    PeriodicTask.objects.create(
        interval=schedule,
        name=task_name,
        task='ticket_system.events.tasks.send_notification',  
        args=json.dumps(['event_reminder', 'Event reminder message', '1'])
    )