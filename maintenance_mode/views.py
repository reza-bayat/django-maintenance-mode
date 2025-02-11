from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser)
def toggle_maintenance_mode(request):
    current_mode = getattr(settings, 'MAINTENANCE_MODE', False)
    settings.MAINTENANCE_MODE = not current_mode
    return JsonResponse({'status': 'success', 'maintenance_mode': not current_mode})