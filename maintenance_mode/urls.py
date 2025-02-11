from django.urls import path
from maintenance_mode.views import toggle_maintenance_mode

urlpatterns = [
    path('toggle-maintenance/', toggle_maintenance_mode, name='toggle_maintenance'),
]