from django.test import TestCase, RequestFactory
from maintenance_mode.middleware import MaintenanceModeMiddleware

class MaintenanceModeMiddlewareTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_admin_access(self):
        request = self.factory.get('/admin/')
        middleware = MaintenanceModeMiddleware(lambda req: None)
        with self.settings(MAINTENANCE_MODE=True):
            response = middleware(request)
            self.assertNotEqual(response.status_code, 503)  # دسترسی مجاز

def test_allowed_urls(self):
    request = self.factory.get('/api/')
    middleware = MaintenanceModeMiddleware(lambda req: None)
    with self.settings(MAINTENANCE_MODE=True, MAINTENANCE_ALLOWED_URLS=['/api/']):
        response = middleware(request)
        self.assertNotEqual(response.status_code, 503)  # دسترسی مجاز            

def test_access_with_token(self):
    request = self.factory.get('/?token=my-secret-token')
    middleware = MaintenanceModeMiddleware(lambda req: None)
    with self.settings(MAINTENANCE_MODE=True, MAINTENANCE_ACCESS_TOKEN='my-secret-token'):
        response = middleware(request)
        self.assertNotEqual(response.status_code, 503)  # دسترسی مجاز