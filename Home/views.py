import os

from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from getenv import env

from firebase.connector import FireBaseConnector
from .setting_dicts import random, slider_values, make_drop_down


def init_firebasae(options):
    FBC = FireBaseConnector(credential_path=options['credential_path'], database_url=options['databaseURL'],
                            debug=options['debug'])
    ADDITIONAL_SETTINGS = make_drop_down(FBC.init_attributes())
    os.environ['ADDITIONAL_SETTINGS'] = str(ADDITIONAL_SETTINGS)

    FBC.start()

def get_val_from_env(key_name: str):
    return env(key_name)


def get_metior_value():
    return bool(env('show_metior'))


def index(request):
    # if you want to get environment variable
    ADDITIONAL_SETTINGS = get_val_from_env('ADDITIONAL_SETTINGS')
    print(ADDITIONAL_SETTINGS)

    context = {
        'sliders': slider_values,
        "drop_down": ADDITIONAL_SETTINGS,
        'random': random,
    }
    return render(request, 'home/index.html', context=context)


def render_setting(request):
    print(request.GET)
    setting_name = request.GET.get('setting_name', '')
    ADDITIONAL_SETTINGS = get_val_from_env('ADDITIONAL_SETTINGS')

    setting_html = ''
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
