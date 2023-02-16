from django.core.management.base import BaseCommand

from task_app import kettle


class Command(BaseCommand):
    def handle(self, *args, **options):
        start = kettle.Kettle()
        start.start_boiling()
