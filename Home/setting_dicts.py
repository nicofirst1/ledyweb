drop_down = [
    {
        'Name': 'Metior',
        'inputs': [
            {
                'type': 'slider',
                'label': 'size',
                'initial_value': 0,
                'min': 0,
                'max': 100
            },
            {
                'type': 'switch',
                'label': 'random decay',
                'initial_value': 'on'
            },
            {
                'type': 'string',
                'label': 'Str Input',
                'initial_value': 'Some string '
            },
        ]
    },
    {
        'Name': 'Fading',
        'inputs': [
            {
                'type': 'slider',
                'label': 'points',
                'initial_value': 0,
                'min': 0,
                'max': 100
            },
            {
                'type': 'slider',
                'label': 'delay start',
                'initial_value': 0,
                'min': 0,
                'max': 100
            },
            {
                'type': 'slider',
                'label': 'delay end',
                'initial_value': 0,
                'min': 0,
                'max': 100
            },

        ]
    },
    # please populate more over here
]
random = True  # set values as per you want below if random
slider_values = {
    'delay': {
        'min': 0,
        'max': 100,
        'current': 23
    },
    'red': {
        'min': 0,
        'max': 255,
        'current': 23
    },
    'green': {
        'min': 0,
        'max': 255,
        'current': 23
    },
    'blue': {
        'min': 0,
        'max': 255,
        'current': 40

    },
    'alpha': {
        'min': 0,
        'max': 255,
        'current': 23
    },
}
