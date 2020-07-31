from logging import getLogger

from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from getenv import env

from Home.views import FV

django_logger = getLogger('django_logger')




def get_val_from_env(key_name: str):
    return env(key_name)


def index(request):
    # if you want to get environment variable
    additional_settings = get_val_from_env('ADDITIONAL_SETTINGS')
    settings = get_val_from_env('SETTINGS')

    settings = dict(settings)
    additional_settings = list(additional_settings)

    context = {
        'settings': settings,
        "drop_down": additional_settings,
    }
    return render(request, 'home/index.html', context=context)


def render_setting(request):
    print(f"Request in render_settings:\n{request.GET}")

    pattern = request.GET.get('cur_pattern', '')
    additional_settings = get_val_from_env('ADDITIONAL_SETTINGS')
    additional_settings = list(additional_settings)

    for setting in additional_settings:
        if setting['Name'].__contains__(pattern):
            setting_html = render_to_string('home/setting_form.html', setting)
            response = {
                'success': True,
                'value': setting_html,
            }
            return JsonResponse(response, safe=False)
    return JsonResponse({'success': False, 'value': None})


def get_form_values(request):
    values = request.GET.dict()
    django_logger.debug(f"Request in get_form_values:\n{values}")
    FV.process_request(request)

    # Your code here
    response = {
        'success': True,
        'value': values,
    }
    return JsonResponse(response, safe=False)
