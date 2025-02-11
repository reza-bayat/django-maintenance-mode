from django.conf import settings
from django.shortcuts import render

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, 'MAINTENANCE_MODE', False):
            allowed_urls = getattr(settings, 'MAINTENANCE_ALLOWED_URLS', [])
            if any(request.path.startswith(url) for url in allowed_urls):
                return self.get_response(request)

            allowed_ips = getattr(settings, 'MAINTENANCE_ALLOWED_IPS', [])
            if request.META.get('REMOTE_ADDR') in allowed_ips:
                return self.get_response(request)

            access_token = getattr(settings, 'MAINTENANCE_ACCESS_TOKEN', None)
            if access_token and request.GET.get('token') == access_token:
                return self.get_response(request)

            if request.user.is_authenticated:
                allowed_users = getattr(settings, 'MAINTENANCE_ALLOWED_USERS', [])
                if request.user.username in allowed_users or request.user.is_staff:
                    return self.get_response(request)

            maintenance_template = getattr(settings, 'MAINTENANCE_TEMPLATE', 'maintenance_mode/maintenance.html')
            return render(request, maintenance_template, status=503)
        
        return self.get_response(request)