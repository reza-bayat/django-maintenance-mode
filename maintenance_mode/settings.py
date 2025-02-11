DEFAULT_SETTINGS = {
    'MAINTENANCE_MODE': False, 
    'MAINTENANCE_ALLOWED_IPS': [],
    'MAINTENANCE_ALLOWED_USERS': [],
    'MAINTENANCE_ACCESS_TOKEN': None, 
    'MAINTENANCE_ALLOWED_URLS': ['/admin/', '/api/'], 
    'MAINTENANCE_TEMPLATE': 'maintenance.html', 
}

def apply_default_settings():
    from django.conf import settings as django_settings
    for key, value in DEFAULT_SETTINGS.items():
        if not hasattr(django_settings, key):
            setattr(django_settings, key, value)