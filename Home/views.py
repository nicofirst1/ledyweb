import os
from logging import getLogger

from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from getenv import env

from firebase.connector import FireBaseConnector
from .setting_dicts import parse_additional_settings, parse_settings

django_logger = getLogger('django_logger')


class TMP:

    def __init__(self):
        self.fbc = None

    def init_firebasae(self, options):
        fbc = FireBaseConnector(credential_path=options['credential_path'], database_url=options['databaseURL'],
                                debug=options['debug'])
        additional_settings = parse_additional_settings(fbc.init_attributes())
        settings = parse_settings(fbc)
        os.environ['ADDITIONAL_SETTINGS'] = str(additional_settings)
        os.environ['SETTINGS'] = str(settings)

        # start firebase
        fbc.start()

        self.fbc = fbc

    def process_request(self, request):
        values = request.GET.dict()
        print(f"Values recived : {values}")
        a=1



tmp = TMP()


def get_val_from_env(key_name: str):
    return env(key_name)


def index(request):
    # if you want to get environment variable
    additional_settings = get_val_from_env('ADDITIONAL_SETTINGS')
    settings = get_val_from_env('SETTINGS')

    #additional_settings = dict(additional_settings)
    settings = dict(settings)

    context = {
        'settings': settings,
        "drop_down": additional_settings,
    }
    return render(request, 'home/index.html', context=context)


def render_setting(request):
    django_logger.debug(f"Request in render_settings:\n{request.GET}")

    setting_name = request.GET.get('setting_name', '')
    additional_settings = get_val_from_env('ADDITIONAL_SETTINGS')


    for setting in additional_settings:
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
    django_logger.debug(f"Request in get_form_values:\n{values}")
    tmp.process_request(request)

    # Your code here
    response = {
        'success': True,
        'value': values,
    }
    return JsonResponse(response, safe=False)
