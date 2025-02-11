from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Toggle maintenance mode on or off'

    def handle(self, *args, **options):
        current_mode = getattr(settings, 'MAINTENANCE_MODE', False)
        settings.MAINTENANCE_MODE = not current_mode
        self.stdout.write(self.style.SUCCESS(f'Maintenance mode is now {"ON" if not current_mode else "OFF"}'))