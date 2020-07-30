from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from getenv import env
import os
from .setting_dicts import drop_down, random, slider_values


def get_val_from_env(key_name: str):
    return env(key_name)


def get_metior_value():
    return bool(env('show_metior'))


def index(request):
    # if you want to get environment variable
    # env_variable = get_val_from_env('my_env')
    # print(env_variable)

    context = {
        'sliders': slider_values,
        "drop_down": drop_down,
        'random': random,
    }
    return render(request, 'home/index.html', context=context)


def render_setting(request):
    print(request.GET)
    setting_name = request.GET.get('setting_name', '')
    setting_html = ''
    for setting in drop_down:
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
