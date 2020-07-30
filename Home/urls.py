from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('render_settings', render_setting, name='render_settings'),
    path('get_form_values', get_form_values, name='get_form_values'),
]
