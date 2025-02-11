# Django Maintenance Mode
A simple yet powerful Django package to manage maintenance mode for your website. This package allows you to:

- Enable/disable maintenance mode.
- Customize the maintenance page template.
- Allow specific users, IPs, or URLs to bypass maintenance mode.
- Keep the admin panel and specific URLs accessible during maintenance.

## Installation
Install the package using `pip`:

```bash
pip install django-maintenance-mode
```
Alternatively, if you're installing from a local source:

```bash
pip install -e /path/to/django-maintenance-mode
```

Add `'maintenance_mode'` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'maintenance_mode',
]
```

Add the middleware to your `MIDDLEWARE`:

```python
MIDDLEWARE = [
    ...
    'maintenance_mode.middleware.MaintenanceModeMiddleware',
]
```


## Configuration
You can configure the maintenance mode settings in `settings.py`. Below are the available options:

```python
MAINTENANCE_MODE = True  # Enable maintenance mode (default: False)
MAINTENANCE_ALLOWED_IPS = ['127.0.0.1', '192.168.1.1']  # List of allowed IPs
MAINTENANCE_ALLOWED_USERS = ['admin', 'superuser']      # List of allowed usernames
MAINTENANCE_ACCESS_TOKEN = 'my-secret-token'            # Access token for bypassing maintenance mode
MAINTENANCE_ALLOWED_URLS = ['/admin/', '/api/']         # URLs always accessible
MAINTENANCE_TEMPLATE = 'custom_maintenance.html'        # Path to your custom maintenance template
```

## Default Settings
If no configuration is provided, the following defaults will be used:

```python
MAINTENANCE_MODE = False
MAINTENANCE_ALLOWED_IPS = []
MAINTENANCE_ALLOWED_USERS = []
MAINTENANCE_ACCESS_TOKEN = None
MAINTENANCE_ALLOWED_URLS = ['/admin/']
MAINTENANCE_TEMPLATE = 'maintenance.html'
```

## Usage
**1- Enabling/Disabling Maintenance Mode**
To enable maintenance mode, set `MAINTENANCE_MODE` to True in your `settings.py`:
```python
MAINTENANCE_MODE = True
```
Alternatively, you can toggle maintenance mode dynamically using a view:

```python
from django.urls import path
from maintenance_mode.views import toggle_maintenance_mode

urlpatterns = [
    path('toggle-maintenance/', toggle_maintenance_mode, name='toggle_maintenance'),
]
```

Visit `/toggle-maintenance/` as a superuser to toggle the maintenance mode.

Using Management Command
You can also toggle maintenance mode using the following management command:

```bash
python manage.py toggle_maintenance
```

This command will switch the maintenance mode on or off and display the current status in the terminal:


```bash
Maintenance mode is now ON
```

**2- Custom Maintenance Template**

You can specify a custom template for the maintenance page by setting the `MAINTENANCE_TEMPLATE` in your settings:

```python
MAINTENANCE_TEMPLATE = 'custom_maintenance.html'  # Path to your custom template
```

The default template is `maintenance.html`. If you provide a custom template, ensure it exists in your templates directory.

**Example Custom Template** `(templates/custom_maintenance.html)`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Maintenance Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        p {
            color: #666;
        }
    </style>
</head>
<body>
    <h1>We are currently under maintenance</h1>
    <p>Please check back later. Thank you for your patience!</p>
</body>
</html>
```

**3- Bypassing Maintenance Mode**

### Allowed IPs

Specify a list of IP addresses that can bypass maintenance mode:

```python
MAINTENANCE_ALLOWED_IPS = ['127.0.0.1', '192.168.1.1']
```

### Allowed Users

Specify a list of usernames that can bypass maintenance mode:

```python
MAINTENANCE_ALLOWED_USERS = ['admin', 'superuser']
```

### Access Token
Provide an access token to bypass maintenance mode via URL:

```bash
http://example.com/?token=my-secret-token
```

Set the token in your settings:

```python
MAINTENANCE_ACCESS_TOKEN = 'my-secret-token'
```

Allowed URLs

Specify URLs that should remain accessible during maintenance mode:

```python
MAINTENANCE_ALLOWED_URLS = ['/admin/', '/api/', '/health-check/']
```

**4- Admin Panel Access**

The admin panel (`/admin/`) is always accessible during maintenance mode by default. You can customize this behavior by modifying the `MAINTENANCE_ALLOWED_URLS` setting.


### Testing
To test the package, you can use the following commands:

```bash
python manage.py test maintenance_mode
```

**Example Test Case**

```python
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
            self.assertNotEqual(response.status_code, 503)  # Admin panel should be accessible

    def test_custom_template(self):
        request = self.factory.get('/')
        middleware = MaintenanceModeMiddleware(lambda req: None)
        with self.settings(
            MAINTENANCE_MODE=True,
            MAINTENANCE_TEMPLATE='custom_maintenance.html'
        ):
            response = middleware(request)
            self.assertContains(response, "We are currently under maintenance", status_code=503)
```
