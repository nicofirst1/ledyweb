import os

from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from getenv import env

from firebase.connector import FireBaseConnector
from .setting_dicts import parse_additional_settings, parse_settings

def init_firebasae(options):
    FBC = FireBaseConnector(credential_path=options['credential_path'], database_url=options['databaseURL'],
                            debug=options['debug'])
    ADDITIONAL_SETTINGS = parse_additional_settings(FBC.init_attributes())
    SETTINGS = parse_settings(FBC)
    os.environ['ADDITIONAL_SETTINGS'] = str(ADDITIONAL_SETTINGS)
    os.environ['SETTINGS'] = str(SETTINGS)

    FBC.start()


def get_val_from_env(key_name: str):
    return env(key_name)


def index(request):
    # if you want to get environment variable
    ADDITIONAL_SETTINGS = get_val_from_env('ADDITIONAL_SETTINGS')
    SETTINGS = get_val_from_env('SETTINGS')
    print(ADDITIONAL_SETTINGS)

    context = {
        'settings': SETTINGS,
        "drop_down": ADDITIONAL_SETTINGS,
    }
    return render(request, 'home/index.html', context=context)


def render_setting(request):
    print(request.GET)
    setting_name = request.GET.get('setting_name', '')
    ADDITIONAL_SETTINGS = get_val_from_env('ADDITIONAL_SETTINGS')

    for setting in ADDITIONAL_SETTINGS:
        if setting['Name'].__contains__(setting_name):
            setting_html = render_to_string('home/setting_form.html', setting)
            response = {
                'success': True,
                'value': setting_html,
            }
            return JsonResponse(response, safe=False)
    return JsonResponse({'success': False, 'value': None})


def get_form_values(request):
    values = request.GET.dict()
    print(values)  # values in dict
    # Your code here
    response = {
        'success': True,
        'value': values,
    }
    return JsonResponse(response, safe=False)
