from django.apps import AppConfig

class MaintenanceModeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'maintenance_mode'

    def ready(self):
        from .settings import apply_default_settings
        apply_default_settings()